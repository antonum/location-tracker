#!/bin/bash

# Location Tracker App Startup Script

echo "🚀 Starting Location Tracker App..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Start the services
echo "🐳 Starting services with Docker Compose..."
docker-compose up --build

echo "✅ Services started successfully!"
echo "🌐 Frontend: http://localhost:3000"
echo "🔗 Backend API: http://localhost:5000/api"
echo "🗄️ Database: localhost:5432"
