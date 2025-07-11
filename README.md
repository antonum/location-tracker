# Location Tracker Web App

A full-stack web application with React frontend and Python Flask backend that tracks user locations and displays statistics.

## Features

- **User Registration**: Ask users for their name and location, store with timestamp
- **Recent Users**: Display the last 10 users who registered
- **Location Statistics**: Interactive charts showing user distribution by location (top 10 + others)
- **Real-time Updates**: Data refreshes automatically when new users are added
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

### Backend
- **Python Flask**: Web framework
- **PostgreSQL**: Database
- **psycopg2**: Database adapter
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **React**: User interface
- **Chart.js & React-ChartJS-2**: Data visualization
- **Axios**: HTTP client
- **CSS3**: Styling

## Database Schema

The application uses four main tables:

1. **us_states**: US states with abbreviations
2. **canadian_provinces**: Canadian provinces with abbreviations  
3. **countries**: Countries with ISO codes
4. **user_records**: User entries with name, location, and timestamp

## Setup Instructions

### Prerequisites

- Node.js (v14 or higher)
- Python 3.8+
- PostgreSQL database

### Database Setup

1. Create a PostgreSQL database:
```bash
createdb location_tracker
```

2. Run the schema script:
```bash
psql -d location_tracker -f backend/schema.sql
```

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. Start the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## API Endpoints

### Backend API

- `GET /api/health` - Health check
- `GET /api/locations` - Get all available locations
- `POST /api/users` - Add new user
- `GET /api/users/recent` - Get last 10 users
- `GET /api/users/stats` - Get user statistics by location

### Example API Usage

```bash
# Add a user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "location": "California, USA"}'

# Get recent users
curl http://localhost:5000/api/users/recent

# Get statistics
curl http://localhost:5000/api/users/stats
```

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://username:password@localhost:5432/location_tracker
FLASK_ENV=development
FLASK_DEBUG=True
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000/api
```

## Deployment

### Quick AWS Deployment (Recommended)

The easiest way to deploy is using **AWS App Runner**:

1. **Push to GitHub**:
   ```bash
   git init && git add . && git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/location-tracker.git
   git push -u origin main
   ```

2. **Deploy to App Runner**:
   - Go to AWS Console → App Runner → Create service
   - Connect to your GitHub repository
   - Select "Docker" runtime
   - Use the included `apprunner.yaml` configuration
   - Deploy automatically

3. **Access your app** at the provided App Runner URL

**Cost**: ~$25-50/month for light usage

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

### Local Production Testing

```bash
# Build and run the production container
docker build -t location-tracker .
docker run -p 8080:8080 -e DATABASE_URL="your-db-url" location-tracker
```

### Other AWS Options
- **AWS Lightsail**: $10-20/month (simple containers)
- **AWS ECS Fargate**: $30-60/month (more control)
- **AWS Elastic Beanstalk**: $20-40/month (platform-as-a-service)

### Backend Deployment
- Configure production database URL
- Set `FLASK_ENV=production`
- Use a WSGI server like Gunicorn

### Frontend Deployment
- Run `npm run build` to create production build
- Serve the `build` folder with a web server
- Configure API URL for production

## Development

### Adding New Features
1. Backend: Add new routes in `app.py`
2. Frontend: Create new components in `src/components/`
3. Database: Add migrations if schema changes are needed

### Testing
- Backend: Add tests using pytest
- Frontend: Add tests using React Testing Library

## Troubleshooting

### Common Issues

1. **Database Connection Error**: Check PostgreSQL is running and credentials are correct
2. **CORS Error**: Ensure Flask-CORS is configured properly
3. **Port Conflicts**: Change ports in configuration if needed

### Logs
- Backend logs: Check Flask console output
- Frontend logs: Check browser developer console

## License

This project is licensed under the MIT License.
