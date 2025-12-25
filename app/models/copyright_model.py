## Swagger doc
from pydantic import BaseModel, HttpUrl, Field
from typing import List

class CopyrightCheckRequest(BaseModel):
      image_url: HttpUrl = Field(..., description="Publicly accessible  url of the image to check")

class DetectedKeyword(BaseModel):
      text: str = Field(..., description="Detected keyword")
      confidence: float = Field(..., description="Confidence of the detected keyword, confidence score between 0 and 1")

class CopyrightCheck(BaseModel):
      copyrighted_content: List[DetectedKeyword] = Field(..., description="List of detected keywords that are copyrighted")
      copyright_found: bool = Field(..., description="Whether copyright was found in the image or not")
      extracted_text: str = Field(..., description="Returns the information extracted from the image")

class CopyrightCheckResponse(BaseModel):
      data: CopyrightCheck = Field(..., description="Copyright detection result data")