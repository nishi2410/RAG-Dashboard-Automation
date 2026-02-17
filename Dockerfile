FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (for caching optimization)
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend folder
COPY backend/ .

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
