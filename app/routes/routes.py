# from flask import Blueprint
# from app.controllers.grammar_controller import check_grammar, render_suggestion
# from app.controllers.plagiarism_controller import check_plagiarism
# from app.controllers.copyright_check_controller import copyright_check


# grammar_routes = Blueprint("grammar_routes", __name__)
# grammar_routes.route('/check-grammar', methods=['POST'])(check_grammar)
# grammar_routes.route('/render-suggestion', methods=['POST'])(render_suggestion)
# grammar_routes.route('/check_plagiarism', methods=['POST'])(check_plagiarism)
# grammar_routes.route('/check-image-copyright', methods=['POST'])(copyright_check)

#from fastapi import APIRouter, Request
#from app.controllers.grammar_controller import check_grammar, render_suggestion
#from app.controllers.plagiarism_controller import check_plagiarism
#from app.controllers.copyright_check_controller import copyright_check

#router = APIRouter()
from app.controllers import grammar_controller, plagiarism_controller, copyright_check_controller


#router.post("/check-grammar")(check_grammar)
#router.post("/render-suggestion")(render_suggestion)
#router.post("/check-plagiarism")(check_plagiarism)
#router.post("/check-image-copyright")(copyright_check)

def register_routes(app):
    app.include_router(grammar_controller.router)
    app.include_router(plagiarism_controller.router)
    app.include_router(copyright_check_controller.router)

