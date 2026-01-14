"""
Text Preprocessing Module
Provides NLP utilities for text cleaning and tokenization
"""

import re


def preprocess_text(text):
    """
    Preprocesses text by performing basic NLP operations.
    
    Args:
        text (str): Raw input text
        
    Returns:
        dict: Dictionary containing:
            - 'cleaned': Cleaned text
            - 'tokens': List of tokens
            - 'word_count': Number of words
    """
    # Basic cleaning
    cleaned = text.strip()
    
    # Tokenization (simple split by whitespace and punctuation)
    tokens = re.findall(r'\b\w+\b', cleaned.lower())
    
    # Remove stopwords (basic English stopwords)
    stopwords = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for',
        'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on',
        'that', 'the', 'to', 'was', 'will', 'with'
    }
    
    filtered_tokens = [token for token in tokens if token not in stopwords]
    
    return {
        'cleaned': cleaned,
        'tokens': filtered_tokens,
        'word_count': len(tokens)
    }


def extract_sentences(text):
    """
    Splits text into individual sentences.
    
    Args:
        text (str): Input text containing one or more sentences
        
    Returns:
        list: List of sentences
    """
    # Simple sentence splitting based on punctuation
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


def is_valid_requirement(text):
    """
    Checks if the text appears to be a valid requirement statement.
    
    Args:
        text (str): Input text to validate
        
    Returns:
        tuple: (is_valid, message)
    """
    if not text or len(text.strip()) < 10:
        return False, "Requirement is too short (minimum 10 characters)"
    
    if len(text) > 1000:
        return False, "Requirement is too long (maximum 1000 characters)"
    
    # Check if it contains at least some meaningful words
    tokens = re.findall(r'\b\w+\b', text.lower())
    if len(tokens) < 3:
        return False, "Requirement must contain at least 3 words"
    
    return True, "Valid requirement"


def normalize_whitespace(text):
    """
    Normalizes whitespace in text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Text with normalized whitespace
    """
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


if __name__ == "__main__":
    # Test the preprocessor
    test_text = "The system should be fast and user-friendly. Users can login easily."
    
    print("Original text:", test_text)
    print("\nPreprocessed:")
    result = preprocess_text(test_text)
    print(f"Cleaned: {result['cleaned']}")
    print(f"Tokens: {result['tokens']}")
    print(f"Word count: {result['word_count']}")
    
    print("\nSentences:")
    sentences = extract_sentences(test_text)
    for i, sent in enumerate(sentences, 1):
        print(f"{i}. {sent}")
    
    print("\nValidation:")
    is_valid, message = is_valid_requirement(test_text)
    print(f"Valid: {is_valid}, Message: {message}")
