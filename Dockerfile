FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .



# Install libGL and other dependencies needed for OpenCV
RUN apt-get update && \
    apt-get install -y default-jre libgl1 libglib2.0-0 && \
    apt-get install -y libgl1 libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip


COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

