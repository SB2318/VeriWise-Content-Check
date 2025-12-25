# Initialize Flask
# from flask import Flask

# def create_app():
#   app = Flask(__name__)
    # register grammer route
#    from .routes.routes import grammar_routes
#    app.register_blueprint(grammar_routes)
#   return app

from fastapi import FastAPI
from app.routes.routes import register_routes
from fastapi.middleware.cors import CORSMiddleware
def create_app():
    app = FastAPI(
        title="Content Intelligence API",
        description="API for Content verification",
        version="1.0.0",
        root_path="/content-intel"
    )
    origins = [
    "https://veriwise-swagger-ui.vercel.app", 
    'http://127.0.0.1:5500'
    "https://uhsocial.in/content-intel"
    ]
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    register_routes(app)
    return app