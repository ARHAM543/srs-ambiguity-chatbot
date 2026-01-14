"""
Flask Web Application for SRS Ambiguity Detection Chatbot
Interactive clarification-based analysis
"""

from flask import Flask, request, jsonify, send_from_directory, send_file, make_response
from flask_cors import CORS
import os
import uuid
import io
from datetime import datetime

# Import our custom modules
from detector import detect_ambiguity, suggest_improvement, highlight_ambiguous_words
from classifier import classify_requirement, get_confidence_score, get_matched_keywords
from preprocessor import preprocess_text, is_valid_requirement, normalize_whitespace
from clarifications import get_clarification_question, apply_user_clarification
from pdf_generator import generate_improved_srs_pdf

app = Flask(__name__, static_folder='static')
CORS(app)

# Store conversation sessions (in-memory for simplicity)
conversations = {}


@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('static', 'index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Chat endpoint for conversational interaction with clarification support
    
    Expected JSON input:
    {
        "message": "The system should be fast",
        "session_id": "optional-session-id"
    }
    
    Returns:
    {
        "bot_messages": [...],
        "session_id": "...",
        "timestamp": "...",
        "awaiting_clarification": true/false
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Missing required field: message'
            }), 400
        
        user_message = data['message'].strip()
        session_id = data.get('session_id', str(uuid.uuid4()))
        
        # Initialize conversation if new session
        if session_id not in conversations:
            conversations[session_id] = {
                'messages': [],
                'created_at': datetime.now().isoformat(),
                'state': 'initial',  # States: initial, awaiting_clarification, completed
                'pending_clarifications': [],  # ambiguous words needing clarification
                'clarifications': {},  # {ambiguous_word: user_clarification}
                'original_document': None,
                'requirements': [],
                'session_id': session_id  # Store session ID
            }
        
        session = conversations[session_id]
        
        # Add user message to history
        session['messages'].append({
            'role': 'user',
            'content': user_message,
            'timestamp': datetime.now().isoformat()
        })
        
        # Check if we're in clarification mode
        if session['state'] == 'awaiting_clarification':
            # User is providing a clarification
            bot_messages = handle_clarification_response(session, user_message)
        else:
            # User is providing initial SRS document
            bot_messages = generate_bot_response(user_message, session_id, session)
        
        # Add bot messages to history
        for msg in bot_messages:
            session['messages'].append({
                'role': 'bot',
                'content': msg['content'],
                'type': msg.get('type', 'text'),
                'data': msg.get('data'),
                'timestamp': datetime.now().isoformat()
            })
        
        return jsonify({
            'bot_messages': bot_messages,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'awaiting_clarification': session['state'] == 'awaiting_clarification'
        }), 200
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500


def handle_clarification_response(session, user_response):
    """
    Handle user's response to a clarification question
    
    Args:
        session: Current session object
        user_response: User's clarification answer
        
    Returns:
        list: Bot messages
    """
    messages = []
    
    # Get the current ambiguous term we're clarifying
    current_word = session['pending_clarifications'][0]
    
    # Store the user's clarification
    session['clarifications'][current_word] = user_response
    
    # Remove from pending list
    session['pending_clarifications'].pop(0)
    
    # Thank user
    messages.append({
        'content': f'✅ Got it! I\'ll use **"{user_response}"** instead of "{current_word}".',
        'type': 'text'
    })
    
    # Check if more clarifications are needed
    if session['pending_clarifications']:
        # Ask next question
        next_word = session['pending_clarifications'][0]
        question = get_clarification_question(next_word)
        messages.append({
            'content': f'📝 Next ambiguous term: **"{next_word}"**\n\n{question}',
            'type': 'text'
        })
    else:
        # All clarifications received, generate final improvements
        session['state'] = 'completed'
        messages.extend(generate_final_improvements(session))
    
    return messages


def generate_final_improvements(session):
    """
    Generate final improved requirements using user clarifications
    
    Args:
        session: Session with all clarifications
        
    Returns:
        list: Bot messages with final improvements
    """
    messages = []
    
    messages.append({
        'content': '🎉 **All clarifications received!** Generating your improved SRS...\n',
        'type': 'text'
    })
    
    # Apply clarifications to each requirement
    improved_requirements = []
    
    for req_data in session['requirements']:
        improved_text = req_data['original']
        
        # Apply each user clarification
        for ambiguous_word in req_data['ambiguous']:
            if ambiguous_word in session['clarifications']:
                user_clarification = session['clarifications'][ambiguous_word]
                improved_text = apply_user_clarification(improved_text, ambiguous_word, user_clarification)
        
        improved_requirements.append({
            'original': req_data['original'],
            'improved': improved_text,
            'category': req_data['category']
        })
    
    # Show improved requirements
    improvement_parts = ['✨ **Your Improved Requirements:**\n']
    
    for i, req in enumerate(improved_requirements[:10], 1):  # Show max 10
        if req['original'] != req['improved']:
            improvement_parts.append(f'**{i}. {req["category"]}**')
            improvement_parts.append(f'   **Before:** {req["original"][:80]}...' if len(req['original']) > 80 else f'   **Before:** {req["original"]}')
            improvement_parts.append(f'   **After:** {req["improved"][:100]}...\n' if len(req['improved']) > 100 else f'   **After:** {req["improved"]}\n')
    
    messages.append({
        'content': '\n'.join(improvement_parts),
        'type': 'text'
    })
    
    # Generate PDF
    try:
        session_id = session.get('session_id')
        if not session_id:
            session_id = str(uuid.uuid4())
            
        pdf_filename = f"improved_srs_{str(session_id)[:8]}.pdf"
            
        pdf_bytes = generate_improved_srs_pdf(session, pdf_filename)
        
        # Store PDF bytes in session (in-memory)
        session['pdf_bytes'] = pdf_bytes
        session['pdf_filename'] = pdf_filename
        
        messages.append({
            'content': f'📄 **PDF Ready for Download!**\n\nYour improved SRS has been generated as a professional PDF document.',
            'type': 'download',
            'data': {
                'session_id': session_id,
                'filename': pdf_filename,
                'download_url': f'/download-pdf/{session_id}'
            }
        })
    except Exception as e:
        print(f"PDF generation error: {e}")
        messages.append({
            'content': f'⚠️ PDF generation encountered an issue: {str(e)}',
            'type': 'text'
        })
    
    messages.append({
        'content': '🎊 **Done!** Your requirements are now clearer and more specific. Feel free to analyze another document! 😊',
        'type': 'text'
    })
    
    return messages


def generate_bot_response(user_message, session_id, session):
    """
    Generate appropriate bot response based on user message
    
    Args:
        user_message: User's input text
        session_id: Current session ID
        session: Session object
        
    Returns:
        list: List of bot message objects
    """
    messages = []
    user_lower = user_message.lower()
    
    # Check if this is a greeting or general message
    greetings = ['hi', 'hello', 'hey', 'start', 'help', 'what can you do']
    if any(greeting in user_lower for greeting in greetings) and len(user_message) < 50:
        messages.append({
            'content': '👋 **Hello!** I\'m your SRS Ambiguity Detection Assistant.\n\nI analyze entire SRS documents with **interactive clarification**:\n• Detect ambiguous terms\n• Ask you for specific values\n• Generate personalized improvements\n• Classify requirements (Functional vs Non-Functional)\n\n📝 **Please paste your complete SRS document** (can contain multiple requirements).',
            'type': 'text'
        })
        session['state'] = 'initial'
        return messages
    
    # Otherwise, treat as SRS document for analysis
    text = normalize_whitespace(user_message)
    
    # Validate minimum length
    if len(text) < 20:
        messages.append({
            'content': '⚠️ **Too short!** Please provide a complete SRS document or at least one full requirement statement (minimum 20 characters).',
            'type': 'text'
        })
        return messages
    
    # Split into individual requirements
    requirements = extract_requirements(text)
    
    if not requirements:
        messages.append({
            'content': '⚠️ **No valid requirements found.** Please provide clear requirement statements.',
            'type': 'text'
        })
        return messages
    
    # Analyze all requirements
    total_requirements = len(requirements)
    functional_count = 0
    non_functional_count = 0
    total_ambiguities = 0
    all_ambiguous_words = set()
    requirement_results = []
    
    for req in requirements:
        # Skip very short lines
        if len(req.strip()) < 15:
            continue
            
        ambiguous_words = detect_ambiguity(req)
        category = classify_requirement(req)
        confidence = get_confidence_score(req, category)
        suggested = suggest_improvement(req)
        
        if category == "Functional Requirement":
            functional_count += 1
        elif category == "Non-Functional Requirement":
            non_functional_count += 1
        
        total_ambiguities += len(ambiguous_words)
        all_ambiguous_words.update(ambiguous_words)
        
        requirement_results.append({
            'original': req,
            'ambiguous': ambiguous_words,
            'category': category,
            'confidence': confidence,
            'suggested': suggested
        })
    
    # Store document and requirements in session
    session['original_document'] = text
    session['requirements'] = requirement_results
    
    # Generate response
    response_parts = []
    
    # 1. Document Summary
    response_parts.append(f'📊 **Document Analysis Complete**')
    response_parts.append(f'Analyzed **{len(requirement_results)} requirements** from your SRS document.\n')
    
    # 2. Classification Summary with Explanation
    response_parts.append('📋 **Classification Results:**')
    response_parts.append(f'• **Functional Requirements (FR): {functional_count}**')
    response_parts.append('  _FR specify what the system should DO (features, actions, functions)_')
    response_parts.append(f'• **Non-Functional Requirements (NFR): {non_functional_count}**')
    response_parts.append('  _NFR specify how the system should BE (quality, performance, security)_\n')
    
    # Combine into single message
    messages.append({
        'content': '\n'.join(response_parts),
        'type': 'text'
    })
    
    # 3. Handle ambiguities with interactive clarification
    if total_ambiguities > 0:
        # Notify about ambiguities
        top_ambiguous = list(all_ambiguous_words)[:8]
        ambiguous_list = ', '.join([f'"{w}"' for w in top_ambiguous])
        messages.append({
            'content': f'⚠️ **Found {total_ambiguities} ambiguous terms:** {ambiguous_list}{"..." if len(all_ambiguous_words) > 8 else ""}\n\n💬 **Let me clarify these with you!** I\'ll ask a few quick questions to make your requirements more specific.',
            'type': 'text'
        })
        
        # Set up clarification flow
        session['pending_clarifications'] = list(all_ambiguous_words)[:10]  # Max 10 clarifications
        session['state'] = 'awaiting_clarification'
        
        # Ask first clarification question
        first_word = session['pending_clarifications'][0]
        question = get_clarification_question(first_word)
        messages.append({
            'content': f'📝 **First ambiguous term: "{first_word}"**\n\n{question}',
            'type': 'text'
        })
    else:
        # No ambiguities - document is clear
        messages.append({
            'content': '✅ **No ambiguous terms detected!** Your requirements are well-defined.\n\n🎉 **Excellent!** Your SRS is clear and well-structured. Feel free to analyze another document! 😊',
            'type': 'text'
        })
        session['state'] = 'completed'
    
    return messages


def extract_requirements(text):
    """
    Extract individual requirements from SRS document
    
    Args:
        text: Full SRS document text
        
    Returns:
        list: Individual requirement statements
    """
    import re
    
    # Split by common delimiters
    # Try numbered lists first (1., 2., etc or 1), 2), etc)
    numbered_pattern = r'\d+[\.)]\s+'
    if re.search(numbered_pattern, text):
        requirements = re.split(numbered_pattern, text)
        requirements = [r.strip() for r in requirements if r.strip()]
    # Try bullet points
    elif '•' in text or '*' in text or '-' in text[:50]:
        requirements = re.split(r'[•\*\-]\s+', text)
        requirements = [r.strip() for r in requirements if r.strip()]
    # Split by sentences
    else:
        requirements = re.split(r'[.!?]+', text)
        requirements = [r.strip() for r in requirements if r.strip() and len(r.strip()) > 15]
    
    # Filter out very short segments
    requirements = [r for r in requirements if len(r) > 15]
    
    return requirements[:50]  # Limit to 50 requirements to avoid overwhelming


@app.route('/welcome', methods=['GET'])
def welcome():
    """Get initial welcome message"""
    return jsonify({
        'messages': [
            {
                'content': '👋 **Hello!** I\'m your SRS Ambiguity Detection Assistant.',
                'type': 'text'
            },
            {
                'content': 'I analyze entire SRS documents with **interactive clarification**:\n• Detect ambiguous terms\n• Ask you for specific values\n• Generate personalized improvements\n• Classify requirements (Functional vs Non-Functional)',
                'type': 'text'
            },
            {
                'content': '📝 **Please paste your complete SRS document** (can contain multiple requirements).',
                'type': 'text'
            }
        ]
    })




@app.route('/download-pdf/<session_id>', methods=['GET'])
def download_pdf(session_id):
    """Download the generated PDF for a session"""
    try:
        if session_id not in conversations:
            return jsonify({'error': 'Session not found'}), 404
            
        session = conversations[session_id]
        
        if 'pdf_bytes' not in session:
             return jsonify({'error': 'PDF not found for this session'}), 404
             
        pdf_bytes = session['pdf_bytes']
        pdf_filename = session.get('pdf_filename', 'improved_srs.pdf')
        
        # serve from memory
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=pdf_filename
        )
    
    except Exception as e:
        return jsonify({'error': f'Download failed: {str(e)}'}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'SRS Ambiguity Detection Chatbot is running',
        'active_sessions': len(conversations)
    }), 200


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    print("=" * 60)
    print("SRS Ambiguity Detection Chatbot - INTERACTIVE MODE")
    print("=" * 60)
    print("Server starting...")
    print("URL: http://127.0.0.1:5000")
    print("API Endpoint: POST /chat")
    print("Welcome: GET /welcome")
    print("Features: Interactive Clarification Questions")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=5000)
