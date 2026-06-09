FROM python:3.10-slim

WORKDIR /app

# 1. install dependencies FIRST (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. then copy code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]