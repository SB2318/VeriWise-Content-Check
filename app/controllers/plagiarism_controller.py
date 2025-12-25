# from flask import request, Response, jsonify
import traceback
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.plagiarism_service import PlagiarismService
from app.models.grammar_plagiarism_model import  GrammarCheckRequestModel, PlagiarismCheckResponseModel
from app.models.error_model import ErrorResponse

router = APIRouter(prefix='/plagiarism', tags=['Plagiarism'])

@router.post('/check',
 summary ='Check for plagiarism in submitted text',
 description='Returns possible plagiarism match percentage, text, and source',
 response_model=PlagiarismCheckResponseModel,
 response_description='Plagiarism check result',
 responses={
        400: {"model": ErrorResponse, "description": "Missing or invalid input"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
 }
)
async def check_plagiarism(request:GrammarCheckRequestModel)->PlagiarismCheckResponseModel:
    
    #data = request.get_json()
    #data = await request.json()
    text = request.text

    if not text:
       # return jsonify({'error': 'Missing text'}), 400
       return JSONResponse(content={'error': 'Missing text'}, status_code=400)

    #text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = PlagiarismService().check_plagiarism(text)
     # return jsonify({'data': corrected}), 200
     return JSONResponse(content={'data': corrected}, status_code=200)

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     print("Error occurred:", e)
     traceback.print_exc()
     return JSONResponse(content={'error': str(e)}, status_code=500)



