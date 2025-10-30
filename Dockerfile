FROM python:3.12-slim

WORKDIR /app

# pip-i yeniləyirik
RUN python -m pip install --upgrade pip

# packages quraşdırılır
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# source kodunu kopyalayırıq
COPY . .

# Consumer + FastAPI server eyni konteynerdə işləyəcək
CMD ["sh", "-c", "python consumer.py & uvicorn web_server:app --host 0.0.0.0 --port 8001"]
