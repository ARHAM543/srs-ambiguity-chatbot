# 🤖 SRS Ambiguity Detection Chatbot

An AI-powered **conversational chatbot** that analyzes Software Requirements Specification (SRS) sentences through natural chat interactions. The bot detects ambiguous terms, classifies requirements, and suggests improvements.

## ✨ Features

- **💬 Conversational Interface**: Natural chat-based interaction
- **🎯 Ambiguity Detection**: Identifies vague terms like "fast", "user-friendly", "secure"
- **📊 Requirement Classification**: Categorizes as Functional or Non-Functional
- **💡 Smart Suggestions**: Provides specific, measurable alternatives
- **🎨 Modern Chat UI**: Message bubbles, typing indicators, smooth animations
- **📱 Responsive Design**: Works on desktop, tablet, and mobile

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed
- **pip** package manager

### Installation & Running

1. **Open Terminal/Command Prompt** and navigate to the project folder:
   ```bash
   cd "c:\Users\Dell\Desktop\Projects\SRS ambiguity Chatbot"
   ```

2. **Install Dependencies** (one-time setup):
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Server**:
   ```bash
   python app.py
   ```

4. **Open Your Browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

5. **Start Chatting**! The bot will greet you automatically.

### To Stop the Server

Press `Ctrl+C` in the terminal where the server is running.

## 💬 How to Use

### 1. Initial Greeting
When you load the page, the bot will automatically greet you:
```
Bot: 👋 Hello! I'm your SRS Ambiguity Detection Assistant.
Bot: I can help you identify and fix ambiguous requirements...
Bot: Please paste your requirement text, and I'll analyze it for you! 📝
```

### 2. Send a Requirement
Type or paste your SRS requirement in the input box and press Enter or click Send:
```
You: The system should be fast and user-friendly.
```

### 3. Get Analysis
The bot will analyze and respond with:
- Detected ambiguous words
- Classification (FR/NFR)
- Confidence score
- Improved suggestion

```
Bot: Thanks for sharing! Let me analyze your requirement...
Bot: ⚠️ I found 2 ambiguous terms:
Bot:   • "fast" - too vague or unclear
Bot:   • "user-friendly" - too vague or unclear
Bot: 🎯 Classification: Non-Functional Requirement
Bot: Confidence: 100%
Bot: ✨ Here's a clearer version:
Bot: The system should respond within 2 seconds with clear navigation, tooltips, and help documentation.
```

## 📝 Example Requirements to Try

### Functional Requirements:
```
The user can login to the system using email and password.
Users can create, edit, and delete blog posts.
The system shall generate monthly reports automatically.
```

### Non-Functional Requirements:
```
The system should be fast and user-friendly.
The application must have good performance and security.
The interface should be intuitive and easy to use.
```

## 🔧 Environment & Technical Details

### Project Structure
```
SRS ambiguity Chatbot/
├── app.py                 # Flask server with /chat API
├── detector.py            # Ambiguity detection logic
├── classifier.py          # FR/NFR classification
├── preprocessor.py        # Text preprocessing
├── requirements.txt       # Python dependencies
├── static/
│   ├── index.html        # Chat interface
│   ├── style.css         # Chat styling
│   └── script.js         # Chat logic
└── README.md             # This file
```

### Technology Stack

**Backend:**
- **Python 3.8+**
- **Flask 3.0.0** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

**Frontend:**
- **HTML5** - Structure
- **CSS3** - Styling (no framework needed)
- **Vanilla JavaScript** - Client-side logic

**NLP Approach:**
- **Rule-based** pattern matching (no external AI API needed)
- **No internet required** (runs entirely locally)

### Environment Setup

**No virtual environment required**, but recommended for clean Python package management:

```bash
# Optional: Create virtual environment
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### API Endpoints

**POST `/chat`** - Main chat endpoint
```json
Request:
{
  "message": "The system should be fast",
  "session_id": "optional-uuid"
}

Response:
{
  "bot_messages": [...],
  "session_id": "uuid",
  "timestamp": "2024-01-13T..."
}
```

**GET `/welcome`** - Get initial greeting messages

**GET `/health`** - Health check endpoint

## 🧪 Manual Testing Guide

### Basic Testing Checklist

1. **Start Server**
   - Run `python app.py`
   - Verify you see: "SRS Ambiguity Detection Chatbot - CHAT MODE"
   - Check URL: http://127.0.0.1:5000

2. **Load Page**
   - Open browser to http://127.0.0.1:5000
   - Verify bot greeting appears automatically
   - Check chat interface loads properly

3. **Test Greeting**
   - Type "hi" and send
   - Verify bot responds with welcome message

4. **Test Ambiguity Detection**
   - Send: "The system should be fast and user-friendly."
   - Verify:
     - ✅ Detects "fast" and "user-friendly"
     - ✅ Shows classification
     - ✅ Provides improved version

5. **Test Classification**
   - **Functional**: "The user can login to the system."
   - **Non-Functional**: "The system must be secure."
   - Verify correct categorization

6. **Test Multiple Messages**
   - Send several requirements in sequence
   - Verify conversation history persists
   - Check scrolling works properly

### Troubleshooting

**Problem**: "Module not found" error
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: Port 5000 already in use
- **Solution**: Change port in `app.py` line 243: `app.run(debug=True, port=5001)`

**Problem**: Styles not loading
- **Solution**: Hard refresh browser (Ctrl+Shift+R)

**Problem**: Bot not responding
- **Solution**: Check terminal for errors, restart server

## 🎨 Chat Features

- **Real-time Typing Indicator**: Shows when bot is "thinking"
- **Auto-scroll**: Automatically scrolls to newest message
- **Message Bubbles**: Distinct styling for bot vs user
- **Smooth Animations**: Message slide-ins and transitions
- **Character Counter**: Shows 0/1000 characters
- **Keyboard Shortcuts**: Press Enter to send, Shift+Enter for new line

## 🌟 Future Enhancements

- [ ] OpenAI integration for enhanced suggestions
- [ ] Export chat history
- [ ] PDF/TXT file upload
- [ ] Multi-language support
- [ ] Voice input
- [ ] Save/load sessions

## 📄 License

Educational project for Software Requirements Engineering.

---

**Built with ❤️ for clearer requirements!**

Need help? Just type "hi" or "help" in the chat! 💬
