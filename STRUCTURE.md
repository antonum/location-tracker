# Project Structure

```
AWS-Demo/
├── README.md                   # Main documentation
├── SETUP.md                   # Quick setup guide
├── docker-compose.yml         # Docker orchestration
├── start.sh                   # Startup script
├── test_api.py               # API testing script
├── .gitignore                # Git ignore rules
│
├── backend/                   # Python Flask backend
│   ├── app.py                # Main Flask application
│   ├── schema.sql            # Database schema and sample data
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile           # Docker configuration
│   ├── .env                 # Environment variables (create from .env.example)
│   └── .env.example         # Environment variables template
│
└── frontend/                 # React frontend
    ├── package.json          # Node.js dependencies
    ├── Dockerfile           # Docker configuration
    ├── public/
    │   └── index.html       # HTML template
    └── src/
        ├── index.js         # React entry point
        ├── index.css        # Global styles
        ├── App.js           # Main React component
        ├── services/
        │   └── api.js       # API service layer
        └── components/
            ├── UserForm.js      # User input form
            ├── RecentUsers.js   # Recent users display
            └── LocationChart.js # Statistics chart
```

## Key Files

### Backend (`backend/`)
- **`app.py`**: Main Flask application with all API endpoints
- **`schema.sql`**: Database schema and sample data for US states, Canadian provinces, and countries
- **`requirements.txt`**: Python dependencies (Flask, psycopg2, etc.)

### Frontend (`frontend/`)
- **`src/App.js`**: Main React component that coordinates the entire application
- **`src/components/UserForm.js`**: Form for adding new users
- **`src/components/RecentUsers.js`**: Display of the last 10 users
- **`src/components/LocationChart.js`**: Interactive charts (bar/pie) for location statistics
- **`src/services/api.js`**: API service layer for backend communication

### Configuration
- **`docker-compose.yml`**: Orchestrates PostgreSQL, Flask backend, and React frontend
- **`start.sh`**: One-command startup script
- **`.env.example`**: Template for environment variables
