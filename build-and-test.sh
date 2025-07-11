#!/bin/bash

# Production Build & Test Script for Location Tracker

echo "🚀 Building Location Tracker for Production..."

# Build the Docker image
echo "📦 Building Docker image..."
docker build -t location-tracker .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
    
    echo "🧪 Testing the production build..."
    echo "Starting container on port 8080..."
    
    # Run the container with your database URL
    # NOTE: Replace with your actual database URL or set DATABASE_URL environment variable
    if [ -z "$DATABASE_URL" ]; then
        echo "⚠️  DATABASE_URL environment variable not set!"
        echo "Please set it with: export DATABASE_URL='your-database-connection-string'"
        echo "Or pass it directly to this script"
        exit 1
    fi
    
    docker run -d -p 8080:8080 \
        -e DATABASE_URL="$DATABASE_URL" \
        -e FLASK_ENV="production" \
        -e PORT="8080" \
        --name location-tracker-test \
        location-tracker
    
    echo "⏳ Waiting for container to start..."
    sleep 5
    
    # Test the health endpoint
    echo "🔍 Testing health endpoint..."
    curl -f http://localhost:8080/api/health
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Production build is working!"
        echo "🌐 Visit: http://localhost:8080"
        echo ""
        echo "To stop the test container:"
        echo "docker stop location-tracker-test && docker rm location-tracker-test"
    else
        echo "❌ Health check failed"
        docker logs location-tracker-test
    fi
else
    echo "❌ Docker build failed"
    exit 1
fi
