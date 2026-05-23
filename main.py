import uvicorn
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Force uvicorn to start the app on port 5000 as requested in the README
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)