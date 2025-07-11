# Quick Setup Guide

## Option 1: Docker (Recommended)

The easiest way to run the application is using Docker:

```bash
# Clone or navigate to the project directory
cd AWS-Demo

# Start the application
./start.sh
```

This will:
- Start PostgreSQL database
- Start Python Flask backend
- Start React frontend
- Initialize the database with sample data

Access the application at: http://localhost:3000

## Option 2: Manual Setup

### Prerequisites
- Node.js 16+
- Python 3.8+
- PostgreSQL 12+

### Steps

1. **Database Setup**:
   ```bash
   createdb location_tracker
   psql -d location_tracker -f backend/schema.sql
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your database credentials
   python app.py
   ```

3. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Testing the Application

1. Open http://localhost:3000
2. Fill in the form with a name and location
3. Submit to see the user added to the recent users list
4. Check the chart to see location statistics

## Stopping the Application

Docker: `docker-compose down`
Manual: Stop the processes with Ctrl+C

## Troubleshooting

- **Database connection issues**: Check PostgreSQL is running and credentials are correct
- **Port conflicts**: Change ports in docker-compose.yml or application configs
- **CORS errors**: Ensure backend and frontend URLs are configured correctly
