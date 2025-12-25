from pydantic import BaseModel, HttpUrl, Field

class ErrorResponse(BaseModel):
      error: str
