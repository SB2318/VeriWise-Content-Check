from pydantic import BaseModel, Field
from typing import List

class ReadabilityCheckRequestModel(BaseModel):
    text: str = Field(..., description="Plain text or HTML text input to analyze for readability")

class ReadabilityIssue(BaseModel):
    type: str = Field(..., description="Type of issue: complex_word, long_sentence, long_paragraph, missing_heading")
    text: str = Field(..., description="The problematic text")
    suggestion: str = Field(..., description="Suggestion to fix the issue")
    severity: str = Field(..., description="low / medium / high")

class ReadabilityResult(BaseModel):
    score: float = Field(..., description="Flesch reading ease score (0-100)")
    level: str = Field(..., description="Beginner Friendly / Intermediate / Advanced")
    approved: bool = Field(..., description="Whether the article passes readability standards")
    issues: List[ReadabilityIssue] = Field(..., description="List of detected issues")

class ReadabilityCheckResponseModel(BaseModel):
    data: ReadabilityResult = Field(..., description="Readability analysis result")