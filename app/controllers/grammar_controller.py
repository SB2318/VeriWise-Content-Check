# from flask import request, Response, jsonify
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse

from app.services.grammar_service import GrammarService
from app.models.grammar_plagiarism_model import GrammarCheckRequestModel, GrammarCheckResponseModel, RenderSuggestionModel
from app.models.error_model import ErrorResponse

router = APIRouter(prefix="/grammar", tags=["Grammar"])

@router.post(
'/check-grammar', 
summary='Check grammar score in submitted text',
description='Analyzes submitted content and returns the score and whether it is accepted or not',
response_description = 'Score Card',
response_model = GrammarCheckResponseModel,
responses={
        400: {"model": ErrorResponse, "description": "Missing or invalid input"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
}
)
async def check_grammar(request: GrammarCheckRequestModel)-> GrammarCheckResponseModel:
    # This function checks the grammar of a sentence
    # It will take HTML Text as an input, and convert it to plain text
    # Then it will use the language tool to check the grammar of the text
    # data = request.get_json()
    # data = await request.json()
    text = request.text
    if not text:
        # return jsonify({'error': 'Missing text'}), 400
        return JSONResponse(content={'error': 'Missing text'}, status_code=400)
    # text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = GrammarService().parse_text(text)
     # return jsonify({'corrected': corrected}), 200
     return GrammarCheckResponseModel(corrected=corrected)

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500)



@router.post(
    '/render-suggestions',
    summary='Render suggestions for the given text with highlights',
    description='Accepts a block of text, analyzes it for grammar suggestions, and returns the highlighted response.',
    response_description ='an html page',
    response_model = RenderSuggestionModel,
    responses={
        400: {"model": ErrorResponse, "description": "Missing or invalid input"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)
async def render_suggestion(request:GrammarCheckRequestModel)-> HTMLResponse:

    #data = request.get_json()
    # data = request
    text = request.text
    if not text:
        #return jsonify({'error': 'Missing text'}), 400
        return JSONResponse(content={'error': 'Missing text'}, status_code=400)
    # text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = GrammarService().render_grammar_suggestion(text)
     html_content = corrected['suggestions']
     original_content = corrected['original']
     full_html = f"""
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Grammar Suggestions</title>
        </head>
        <body>
            <h1>Grammar Suggestions (Highlighted)</h1>
            <div>
                <h3>With Suggestions:</h3>
                {html_content}
            </div>
            <hr />
            <div>
                <h3>Original Content:</h3>
                <pre style="white-space: pre-wrap;">{original_content}</pre>
            </div>
        </body>
        </html>
        """
     return RenderSuggestionModel(full_html=full_html, suggestion=html_content)


    except Exception as e:
     #return jsonify({'error-h': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500)
     
     
    