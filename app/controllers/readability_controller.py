from fastapi import APIRouter
from pydantic import BaseModel
import re

# Set up the FastAPI router for this controller
router = APIRouter()

# Define the data schema for incoming requests
class ReadabilityPayload(BaseModel):
    text: str

def calculate_readability(text: str):
    """
    Analyzes content readability and packages difficult lines into 
    styled HTML <span> elements with descriptive tooltips for the editor.
    """
    if not text.strip():
        return {
            "readability_score": 100,
            "reading_time": "0 min read",
            "suggested_html": ""
        }

    # Split into sentences and words
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    words = text.split()
    word_count = len(words)
    
    # Calculate reading time (200 Words Per Minute average)
    reading_time_mins = max(1, round(word_count / 200))
    reading_time_str = f"{reading_time_mins} min read"

    highlighted_sentences = []
    complex_sentence_count = 0

    for sentence in sentences:
        if not sentence.strip():
            continue
            
        sentence_words = sentence.split()
        sentence_word_count = len(sentence_words)
        
        # Flags sentences longer than 18 words, or longer than 12 words with complex terms
        long_words = sum(1 for w in sentence_words if len(w) > 7)
        
        if sentence_word_count > 18 or (sentence_word_count > 12 and long_words > 3):
            complex_sentence_count += 1
            # Wrap in the exact CSS format requested by the mentor
            highlighted_sentence = (
                f"<span style='background-color: rgba(0, 122, 255, 0.15); "
                f"border-bottom: 2px dashed #007AFF; padding: 2px;' "
                f"title='Readability Warning: This sentence is quite long ({sentence_word_count} words). "
                f"Consider breaking it into shorter, clearer pieces.'>{sentence}</span>"
            )
            highlighted_sentences.append(highlighted_sentence)
        else:
            highlighted_sentences.append(sentence)

    suggested_html = "<p>" + " ".join(highlighted_sentences) + "</p>"

    # Global score generation
    if len(sentences) > 0:
        complexity_ratio = complex_sentence_count / len(sentences)
        global_score = max(10, min(100, round(100 - (complexity_ratio * 60))))
    else:
        global_score = 100

    return {
        "readability_score": global_score,
        "reading_time": reading_time_str,
        "suggested_html": suggested_html
    }

# Expose the POST route requested by the mentor
@router.post("/grammar/analyze-readability")
async def analyze_readability(payload: ReadabilityPayload):
    return calculate_readability(payload.text)
