#!/bin/bash

# Environment Setup Script for Location Tracker

echo "🔐 Setting up secure environment variables..."

# Check if .env already exists
if [ -f "backend/.env" ]; then
    echo "⚠️  backend/.env already exists!"
    read -p "Do you want to overwrite it? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Setup cancelled"
        exit 1
    fi
fi

# Create .env from template
cp backend/.env.example backend/.env

echo "✅ Created backend/.env from template"
echo ""
echo "📝 Please edit backend/.env with your database credentials:"
echo ""
echo "DATABASE_URL=postgres://username:password@host:port/database?sslmode=require"
echo ""
echo "🔧 You can edit it now with:"
echo "nano backend/.env"
echo ""
echo "🚀 After editing, you can run:"
echo "./build-and-test.sh  # Test locally"
echo "git add . && git commit -m 'Secure setup' && git push  # Deploy to AWS"
echo ""
echo "⚠️  Remember to set environment variables in AWS App Runner console!"
echo ""
echo "📚 For more info, see SECURITY.md"
