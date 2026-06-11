from app.controllers import (
    grammar_controller, 
    plagiarism_controller, 
    copyright_check_controller,
    readability_controller  # <-- 1. Added your new controller here
)

def register_routes(app):
    app.include_router(grammar_controller.router)
    app.include_router(plagiarism_controller.router)
    app.include_router(copyright_check_controller.router)
    app.include_router(readability_controller.router)  # <-- 2. Registered your new router heres
