## Here as per my application requirement, I will check the image by using their url

# from flask import request, Response, jsonify
from fastapi import  APIRouter, Request
from fastapi.responses import JSONResponse
from app.services.copyright_check_service import CopyrightCheckerService
from app.models.copyright_model import CopyrightCheckRequest, CopyrightCheckResponse
from app.models.error_model import ErrorResponse

router = APIRouter(prefix='/copyright', tags=['Copyright-Checker'])

@router.post(
    '/check-image-copyright',
    summary="Check if an image is copyrighted",
    response_model=CopyrightCheckResponse,
     responses={
        400: {"model": ErrorResponse, "description": "Missing or invalid input"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
   }
)
async def copyright_check(request:CopyrightCheckRequest)->CopyrightCheckResponse:
    
    # data = request.get_json()
    #data = await request.json()
    url = request.image_url
    if not url:
        #return jsonify({'error': 'Missing image url'}), 400
        return JSONResponse(content={'error': 'Missing image url'}, status_code=400)
    #url = data['image_url']
    # Call grammer service to handle the rest
    try:
     corrected = CopyrightCheckerService().detect_copyrighted_text(url)
     # return jsonify({'data': corrected}), 200
     return JSONResponse(content={'data': corrected}, status_code=200, media_type="application/json")

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500, media_type="application/json")


