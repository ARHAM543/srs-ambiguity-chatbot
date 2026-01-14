"""
Clarification questions for ambiguous terms
Maps ambiguous words to specific counter-questions
"""

CLARIFICATION_QUESTIONS = {
    # Performance/Speed terms
    "fast": "⏱️ How fast should it be? (e.g., response time in seconds)",
    "quick": "⏱️ How quick should the response be? (e.g., within X seconds)",
    "slow": "⏱️ What is the acceptable maximum time? (e.g., X seconds)",
    "quickly": "⏱️ How quickly should this happen? (e.g., within X seconds)",
    "rapid": "⏱️ How rapid should the response be? (e.g., X milliseconds)",
    
    # Usability terms
    "user-friendly": "👤 What makes it user-friendly? (e.g., number of clicks, help features, UI standards)",
    "easy": "👤 What defines 'easy'? (e.g., max number of steps, training time required)",
    "simple": "👤 What makes it simple? (e.g., minimal UI elements, single-page design)",
    "intuitive": "👤 What UI standards should it follow? (e.g., Material Design, iOS HIG)",
    "clear": "👤 How should clarity be ensured? (e.g., tooltips, error messages, documentation)",
    
    # Security terms
    "secure": "🔒 What security measures are required? (e.g., encryption type, authentication method)",
    "safe": "🔒 What safety features are needed? (e.g., SSL/TLS, password hashing method)",
    "protected": "🔒 How should data be protected? (e.g., access control method, encryption level)",
    "encrypted": "🔒 What encryption standard? (e.g., AES-256, RSA-2048)",
    
    # Reliability terms
    "reliable": "🎯 What reliability level is required? (e.g., uptime percentage, error rate)",
    "robust": "🎯 What load should it handle? (e.g., concurrent users, requests per second)",
    "stable": "🎯 What stability metrics? (e.g., crash rate, error frequency)",
    
    # Scalability terms
    "scalable": "📈 What scale is needed? (e.g., number of users, data volume)",
    "flexible": "📈 What flexibility features? (e.g., configurable settings, plugin support)",
    "adaptable": "📈 What platforms should it support? (e.g., Web, iOS, Android)",
    
    # Quality terms
    "good": "✨ What defines 'good' quality? (e.g., defect rate, user satisfaction %)",
    "better": "✨ How much better? (e.g., X% faster, Y% fewer errors)",
    "improved": "✨ What improvement metrics? (e.g., X% performance increase)",
    "high quality": "✨ What quality standards? (e.g., ISO, defect rate threshold)",
    "excellent": "✨ What are the excellence criteria? (e.g., benchmark scores, ratings)",
    
    # Size/Quantity terms
    "large": "📏 How large? (e.g., file size in MB/GB, data volume)",
    "small": "📏 How small? (e.g., maximum file size, memory footprint)",
    "big": "📏 How big? (e.g., storage capacity, screen size)",
    "many": "📏 How many? (e.g., exact number or range)",
    "few": "📏 How few? (e.g., maximum count)",
    
    # Time terms
    "as soon as possible": "⏰ What's the deadline? (e.g., within 24 hours, X business days)",
    "asap": "⏰ What's the specific timeframe? (e.g., within X hours)",
    "timely": "⏰ What's the time requirement? (e.g., within X hours, same-day)",
    "recent": "⏰ How recent? (e.g., last X days, current week)",
    
    # Adequacy terms
    "adequate": "📊 What standards should be met? (e.g., industry standard, compliance level)",
    "sufficient": "📊 What level is sufficient? (e.g., test coverage %, resources needed)",
    "appropriate": "📊 What makes it appropriate? (e.g., compliance standards, guidelines)",
    "reasonable": "📊 What are the constraints? (e.g., budget limit, timeline)",
    
    # Performance terms
    "efficient": "⚡ What efficiency metrics? (e.g., resource usage, processing time)",
    "effective": "⚡ What effectiveness criteria? (e.g., accuracy %, success rate)",
    "optimal": "⚡ What optimization targets? (e.g., latency, throughput)",
    "performance": "⚡ What performance benchmarks? (e.g., response time, throughput)",
}


def get_clarification_question(ambiguous_word):
    """
    Get clarification question for an ambiguous term
    
    Args:
        ambiguous_word: The ambiguous term to clarify
        
    Returns:
        str: Clarification question or default question
    """
    word_lower = ambiguous_word.lower()
    
    if word_lower in CLARIFICATION_QUESTIONS:
        return CLARIFICATION_QUESTIONS[word_lower]
    else:
        return f"❓ Can you provide specific criteria for '{ambiguous_word}'? (e.g., measurable values, standards, or benchmarks)"


def apply_user_clarification(original_text, ambiguous_word, user_clarification):
    """
    Replace ambiguous term with user's clarification
    
    Args:
        original_text: Original requirement text
        ambiguous_word: The ambiguous term to replace
        user_clarification: User's specific clarification
        
    Returns:
        str: Updated requirement with user's clarification
    """
    import re
    
    # Create pattern to match the ambiguous word (case-insensitive)
    pattern = re.compile(re.escape(ambiguous_word), re.IGNORECASE)
    
    # Replace with user's clarification
    improved = pattern.sub(user_clarification, original_text, count=1)
    
    return improved
