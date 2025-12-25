from pydantic import BaseModel, HttpUrl, Field

class GrammarCheckRequestModel(BaseModel):
      text: str = Field(..., description="Plain text input or html text input (prefer) to check for grammar issues")

class GrammarCheckResult(BaseModel):
      corrected: bool = Field(..., description="Whether the text has been corrected or not")
      correction_percentage: float = Field(..., description="Percentage of text that has been corrected")
      approved: bool = Field(..., description="Whether the text is approved or not")
      score: float = Field(..., description="Score out of 10")

class GrammarCheckResponseModel(BaseModel):
      corrected: GrammarCheckResult = Field(..., description="Response data")


class PlagiarismCheckResult(BaseModel):
      plagiarised_percentage: float = Field(..., description="Percentage of plagiarised text")
      plagiarised_text: str = Field(..., description="Plagiarised text")
      source_title: str = Field(..., description="Source title")

class PlagiarismCheckResponseModel(BaseModel):
      data: PlagiarismCheckResult = Field(..., description="Response data")


class RenderSuggestionModel(BaseModel):
      full_html : str = Field(..., description="Full HTML of the rendered text")
      suggestion: str = Field(..., description="Suggestion for the text")