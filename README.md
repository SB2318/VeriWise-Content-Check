# 🔍 VeriWise-Content-Checker

## Server is Currently Down (504)

**VeriWise-Content-Checker** is an intelligent, modular Python API system designed to help you validate and verify content efficiently across multiple aspects:

- ✅ **Plagiarism Detection:** Detect content similarity using TF-IDF & cosine similarity algorithms.
- ✅ **Grammar Checking:** Identify grammar and spelling issues using LanguageTool.
- ✅ **Grammar Suggestion:** Provide detailed grammar improvement suggestions.
- ✅ **Copyright and Medical Content Verification:** Extract text from images using Easyocr and OpenCV to cross-check with a database of copyrighted medical content providers.

---

## 📄 API Documentation (Swagger UI)

🔗 [See Documentation](https://veriwise-swagger-ui.vercel.app/)

# 📸 Screenshot Examples

## Copyright Checker


![Screenshot 2025-05-24 002528](https://github.com/user-attachments/assets/00ebaaf9-85c1-42b7-a20a-65126b0baee9)


## Plagiarism Detection:

![Screenshot 2025-05-21 002104](https://github.com/user-attachments/assets/1d037f72-d068-4586-b8f2-d08b25296ef3)

## Grammar Suggestion:

![Screenshot 2025-05-24 015527](https://github.com/user-attachments/assets/2b9f7b3d-5b42-40fa-8c8f-03fbd22fc4b7)


---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

- fastapi
- uvicorn

- easyocr
- opencv-python
- numpy
- requests
- Pillow
- difflib
- beautifulsoup4
- language_tool_python
- scikit-learn
- pocketbase  # Datasource for plagiarism detection
- PyMuPDF
- python-dotenv


You can install all dependencies using:

```
pip install -r requirements.txt

```

## 🚀 How to Run

1. Clone the repository

```
git clone https://github.com/SB2318/VeriWise-Content-Checker.git
cd VeriWise-Content-Checker

```

2. Install the dependencies

```
pip install -r requirements.txt

```

3. Run the application

```
uvicorn main:app --reload

or

python main.py

```
4. Open your web browser and navigate to `http://127.0.0.1:5000`


## 🚀 Run with Docker

Easily build and run the Veriwise Content Checker using Docker.

---

### 🐳 Prerequisites

- ✅ [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
- 🚀 Ensure Docker Desktop is **running** before executing commands.

---
  
### ⚙️ Step 1: Build the Docker Image

   ```
   docker build -t veriwise-content-checker .
   ```

 ### ⚙️ Step 2: Run the app in a docker container 

   ```
    # Option 1: (Detached Mode)
    docker run -d -p 8000:8000 veriwise-content-checker

    # Option 2: Run in Interactive Mode (for development/debugging)

    docker run -it -p 8000:8000 veriwise-content-checker /bin/sh
    In the terminal enter
    uvicorn main:app --reload

   ```
Check api documentation at https://uhsocial.in/content-intel/docs

## ⚙️ Features Overview

- **Plagiarism Detection:** Submit text to check for similarity against existing content.
- **Grammar Check:** Submit text to get a grammar correctness score (predict score).
- **Grammar Suggestion:** Get detailed suggestions to improve grammar and spelling errors.
- **Copyright Checker:** Upload images or text to verify against copyrighted medical content provider data.

## 🙌 Contribution & Feedback

Feel free to open issues or pull requests to improve the system. For feedback or any queries, you can contact the maintainer, via GitHub or email.


