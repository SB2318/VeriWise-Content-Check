from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.readability_service import ReadabilityService
from app.models.readability_model import ReadabilityCheckRequestModel, ReadabilityCheckResponseModel
from app.models.error_model import ErrorResponse

router = APIRouter(prefix="/readability", tags=["Readability"])

@router.post(
    '/analyze',
    summary='Analyze readability of submitted text',
    description='Analyzes submitted content and returns readability score, accessibility level, and detected issues',
    response_description='Readability Analysis Result',
    response_model=ReadabilityCheckResponseModel,
    responses={
        400: {"model": ErrorResponse, "description": "Missing or invalid input"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def analyze_readability(request: ReadabilityCheckRequestModel) -> ReadabilityCheckResponseModel:
    text = request.text
    if not text:
        return JSONResponse(content={'error': 'Missing text'}, status_code=400)
    try:
        result = ReadabilityService().analyze(text)
        return ReadabilityCheckResponseModel(data=result)
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)