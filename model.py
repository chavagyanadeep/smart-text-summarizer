from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    """
    Summarizes the given text using BART model.
    
    Args:
        text: Input text to summarize
        max_length: Maximum length of summary
        min_length: Minimum length of summary
    
    Returns:
        Summarized text as string
    """
    if len(text.split()) < 30:
        return "Text is too short to summarize. Please provide at least 30 words."
    
    result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return result[0]["summary_text"]
