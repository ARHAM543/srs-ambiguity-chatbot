"""
Requirement Classification Module
Classifies requirements as Functional (FR) or Non-Functional (NFR)
"""

# Keywords that indicate Functional Requirements (what the system does)
FUNCTIONAL_KEYWORDS = [
    # User actions
    "login", "register", "sign up", "sign in", "logout",
    "create", "add", "insert", "delete", "remove",
    "update", "edit", "modify", "change",
    "view", "display", "show", "list", "browse",
    "search", "find", "filter", "sort",
    "upload", "download", "export", "import",
    "send", "receive", "submit", "post",
    "calculate", "compute", "process", "generate",
    "validate", "verify", "check", "confirm",
    "approve", "reject", "cancel",
    "notify", "alert", "remind",
    "print", "save", "store",
    "share", "collaborate",
    
    # System features
    "dashboard", "report", "form", "button",
    "menu", "navigation", "link",
    "payment", "checkout", "cart",
    "profile", "account", "settings",
    "notification", "message", "email",
    "database", "record", "entry",
]

# Keywords that indicate Non-Functional Requirements (quality attributes)
NON_FUNCTIONAL_KEYWORDS = [
    # Performance
    "performance", "speed", "response time", "latency",
    "throughput", "load time", "processing time",
    "fast", "quick", "slow", "efficient",
    
    # Security
    "security", "secure", "encryption", "authentication",
    "authorization", "access control", "password",
    "privacy", "confidential", "protected",
    "ssl", "tls", "https", "oauth",
    
    # Reliability
    "reliability", "reliable", "uptime", "availability",
    "fault tolerance", "backup", "recovery",
    "robust", "stable", "consistent",
    
    # Scalability
    "scalability", "scalable", "concurrent users",
    "load balancing", "horizontal scaling",
    
    # Usability
    "usability", "user-friendly", "intuitive", "easy",
    "accessible", "accessibility", "wcag",
    "user experience", "ux", "ui",
    
    # Maintainability
    "maintainability", "maintainable", "modular",
    "extensible", "flexible", "reusable",
    "documentation", "code quality",
    
    # Portability
    "portability", "portable", "cross-platform",
    "compatibility", "compatible", "browser support",
    
    # Compliance
    "compliance", "compliant", "regulation", "standard",
    "gdpr", "hipaa", "iso", "ieee",
]


def classify_requirement(sentence):
    """
    Classifies a requirement as Functional or Non-Functional.
    
    Args:
        sentence (str): The requirement sentence to classify
        
    Returns:
        str: "Functional Requirement", "Non-Functional Requirement", or "Unclassified"
    """
    sentence_lower = sentence.lower()
    
    functional_count = 0
    non_functional_count = 0
    
    # Count matches for functional keywords
    for keyword in FUNCTIONAL_KEYWORDS:
        if keyword in sentence_lower:
            functional_count += 1
    
    # Count matches for non-functional keywords
    for keyword in NON_FUNCTIONAL_KEYWORDS:
        if keyword in sentence_lower:
            non_functional_count += 1
    
    # Determine category based on keyword counts
    if functional_count > non_functional_count:
        return "Functional Requirement"
    elif non_functional_count > functional_count:
        return "Non-Functional Requirement"
    elif functional_count > 0 and functional_count == non_functional_count:
        # In case of tie, default to Functional if both are present
        return "Functional Requirement"
    else:
        return "Unclassified"


def get_confidence_score(sentence, category):
    """
    Calculates a confidence score for the classification.
    
    Args:
        sentence (str): The requirement sentence
        category (str): The assigned category
        
    Returns:
        int: Confidence score (0-100)
    """
    sentence_lower = sentence.lower()
    
    functional_matches = sum(1 for kw in FUNCTIONAL_KEYWORDS if kw in sentence_lower)
    non_functional_matches = sum(1 for kw in NON_FUNCTIONAL_KEYWORDS if kw in sentence_lower)
    
    total_matches = functional_matches + non_functional_matches
    
    if total_matches == 0:
        return 0  # Unclassified
    
    if category == "Functional Requirement":
        confidence = (functional_matches / total_matches) * 100
    elif category == "Non-Functional Requirement":
        confidence = (non_functional_matches / total_matches) * 100
    else:
        confidence = 0
    
    # Boost confidence if there are multiple matches
    if total_matches >= 3:
        confidence = min(confidence + 10, 100)
    
    return int(confidence)


def get_matched_keywords(sentence, category):
    """
    Returns the list of matched keywords for a given category.
    
    Args:
        sentence (str): The requirement sentence
        category (str): The category to check
        
    Returns:
        list: List of matched keywords
    """
    sentence_lower = sentence.lower()
    matched = []
    
    if category == "Functional Requirement":
        keywords = FUNCTIONAL_KEYWORDS
    elif category == "Non-Functional Requirement":
        keywords = NON_FUNCTIONAL_KEYWORDS
    else:
        return matched
    
    for keyword in keywords:
        if keyword in sentence_lower and keyword not in matched:
            matched.append(keyword)
    
    return matched


if __name__ == "__main__":
    # Test the classifier
    test_sentences = [
        "The user can login to the system using email and password.",
        "The system should have good performance and security.",
        "Users can create, edit, and delete blog posts.",
        "The application must be accessible and comply with WCAG 2.1.",
        "This is a random sentence without clear requirements.",
    ]
    
    for sentence in test_sentences:
        print(f"\nSentence: {sentence}")
        category = classify_requirement(sentence)
        confidence = get_confidence_score(sentence, category)
        keywords = get_matched_keywords(sentence, category)
        print(f"Category: {category}")
        print(f"Confidence: {confidence}%")
        print(f"Matched keywords: {keywords}")
