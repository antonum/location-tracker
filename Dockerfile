# Multi-stage build for production deployment
FROM node:18-alpine AS frontend-build

# Build the React frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production
COPY frontend/ ./
RUN npm run build

# Python backend with built frontend
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./

# Copy built frontend
COPY --from=frontend-build /app/frontend/build ./static

# Update Flask app to serve static files
RUN echo "from flask import send_from_directory\n\
@app.route('/', defaults={'path': ''})\n\
@app.route('/<path:path>')\n\
def serve_frontend(path):\n\
    if path != \"\" and os.path.exists(os.path.join('static', path)):\n\
        return send_from_directory('static', path)\n\
    else:\n\
        return send_from_directory('static', 'index.html')" >> app.py

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
