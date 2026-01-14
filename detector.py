"""
Ambiguity Detection Module
Detects ambiguous words in SRS requirements and suggests improvements
"""

# Comprehensive list of ambiguous terms commonly found in requirements
AMBIGUOUS_WORDS = [
    "fast", "quick", "rapid", "slow",
    "user-friendly", "easy", "simple", "intuitive",
    "efficient", "effective", "optimal", "better", "improved",
    "secure", "safe", "protected",
    "reliable", "robust", "stable",
    "scalable", "flexible", "adaptable",
    "adequate", "sufficient", "appropriate",
    "as soon as possible", "asap", "timely",
    "recent", "modern", "latest",
    "high quality", "good", "bad", "poor",
    "large", "small", "big", "tiny",
    "many", "few", "several", "various",
    "etc", "and so on", "and so forth",
    "reasonable", "acceptable", "suitable",
    "maximum", "minimum", "approximately",
    "normal", "usual", "typical",
    "clear", "obvious", "evident",
]

# Mapping of ambiguous terms to specific, measurable alternatives
SUGGESTIONS = {
    "fast": "within 2 seconds",
    "quick": "within 3 seconds",
    "slow": "more than 5 seconds",
    "user-friendly": "with clear navigation, tooltips, and help documentation",
    "easy": "requiring no more than 3 clicks",
    "simple": "with a clean interface and minimal steps",
    "intuitive": "following standard UI patterns (e.g., Material Design)",
    "efficient": "using less than 100MB of memory",
    "effective": "achieving 95% accuracy",
    "optimal": "meeting performance benchmarks of <2s response time",
    "better": "10% faster than the previous version",
    "improved": "with 20% reduced error rate",
    "secure": "using AES-256 encryption and OAuth 2.0 authentication",
    "safe": "with SSL/TLS encryption and password hashing (bcrypt)",
    "protected": "with role-based access control (RBAC)",
    "reliable": "with 99.9% uptime",
    "robust": "handling 1000 concurrent users",
    "stable": "with less than 0.1% crash rate",
    "scalable": "supporting up to 10,000 users",
    "flexible": "with configurable settings and plugin support",
    "adaptable": "supporting multiple platforms (Web, iOS, Android)",
    "adequate": "meeting ISO 25010 quality standards",
    "sufficient": "providing 99.5% test coverage",
    "appropriate": "following WCAG 2.1 AA accessibility guidelines",
    "as soon as possible": "within 24 hours",
    "asap": "within 24 hours",
    "timely": "within the agreed SLA of 48 hours",
    "recent": "from the last 30 days",
    "modern": "supporting current browser versions (Chrome 90+, Firefox 88+)",
    "latest": "the most recent stable version",
    "high quality": "with less than 5 defects per 1000 lines of code",
    "good": "meeting acceptance criteria with 90% user satisfaction",
    "bad": "with error rate exceeding 5%",
    "poor": "below 70% performance benchmark",
    "large": "greater than 1GB",
    "small": "less than 50MB",
    "big": "exceeding 500MB",
    "tiny": "less than 10MB",
    "many": "more than 100 items",
    "few": "fewer than 10 items",
    "several": "between 5 and 15 items",
    "various": "supporting at least 5 different formats",
    "etc": "(please specify all items explicitly)",
    "and so on": "(please list all requirements)",
    "and so forth": "(please enumerate all conditions)",
    "reasonable": "within the budget of $50,000 and 6-month timeline",
    "acceptable": "meeting 85% of user acceptance criteria",
    "suitable": "compliant with industry standards (IEEE, ISO)",
    "maximum": "not exceeding [specify exact limit]",
    "minimum": "at least [specify exact threshold]",
    "approximately": "[specify exact value ± acceptable range]",
    "normal": "under standard operating conditions (20-25°C, <80% humidity)",
    "usual": "following typical usage patterns",
    "typical": "representing 80% of use cases",
    "clear": "with explicit error messages and status indicators",
    "obvious": "following conventional design patterns",
    "evident": "with visible feedback for all user actions",
}


def detect_ambiguity(sentence):
    """
    Detects ambiguous words in a given sentence.
    
    Args:
        sentence (str): The requirement sentence to analyze
        
    Returns:
        list: List of ambiguous words found in the sentence
    """
    found_words = []
    sentence_lower = sentence.lower()
    
    for word in AMBIGUOUS_WORDS:
        if word in sentence_lower:
            # Avoid duplicate detections
            if word not in found_words:
                found_words.append(word)
    
    return found_words


def suggest_improvement(sentence):
    """
    Suggests an improved version of the sentence by replacing ambiguous words.
    
    Args:
        sentence (str): The original requirement sentence
        
    Returns:
        str: Improved sentence with specific alternatives
    """
    improved = sentence
    
    # Sort by length (longest first) to avoid partial replacements
    sorted_suggestions = sorted(SUGGESTIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for ambiguous, specific in sorted_suggestions:
        # Case-insensitive replacement while preserving original case
        if ambiguous.lower() in improved.lower():
            # Find the exact occurrence (case-insensitive)
            import re
            pattern = re.compile(re.escape(ambiguous), re.IGNORECASE)
            improved = pattern.sub(specific, improved, count=1)
    
    return improved


def highlight_ambiguous_words(sentence, ambiguous_words):
    """
    Creates an HTML string with ambiguous words highlighted.
    
    Args:
        sentence (str): The original sentence
        ambiguous_words (list): List of ambiguous words to highlight
        
    Returns:
        str: HTML string with highlighted words
    """
    highlighted = sentence
    
    # Sort by length (longest first) to avoid partial replacements
    sorted_words = sorted(ambiguous_words, key=len, reverse=True)
    
    for word in sorted_words:
        import re
        pattern = re.compile(f'({re.escape(word)})', re.IGNORECASE)
        highlighted = pattern.sub(r'<span class="ambiguous">\1</span>', highlighted)
    
    return highlighted


if __name__ == "__main__":
    # Test the detector
    test_sentences = [
        "The system should be fast and user-friendly.",
        "The login process must be secure and efficient.",
        "The application should load quickly and provide good performance.",
    ]
    
    for sentence in test_sentences:
        print(f"\nOriginal: {sentence}")
        ambiguous = detect_ambiguity(sentence)
        print(f"Ambiguous words: {ambiguous}")
        improved = suggest_improvement(sentence)
        print(f"Suggested: {improved}")
