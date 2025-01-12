FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and .env
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "01_helloworld.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]