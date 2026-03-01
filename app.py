from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import summarize_text

app = FastAPI(
    title="Smart Text Summarizer API",
    description="AI-powered text summarization using HuggingFace BART model",
    version="1.0.0"
)

class TextInput(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

class SummaryOutput(BaseModel):
    original_text: str
    summary: str
    original_word_count: int
    summary_word_count: int

@app.get("/")
def home():
    return {"message": "Welcome to Smart Text Summarizer API 🤖", "status": "running"}

@app.post("/summarize", response_model=SummaryOutput)
def summarize(input: TextInput):
    """
    Takes a long text and returns an AI-generated summary.
    """
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    summary = summarize_text(input.text, input.max_length, input.min_length)
    
    return SummaryOutput(
        original_text=input.text,
        summary=summary,
        original_word_count=len(input.text.split()),
        summary_word_count=len(summary.split())
    )
