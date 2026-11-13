FROM python:3.11-slim

WORKDIR /app

# System libs needed by OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# Install deps first so Docker caches this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY configs/ configs/
COPY models/ models/

EXPOSE 8000
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
