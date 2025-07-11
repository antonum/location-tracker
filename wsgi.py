#!/usr/bin/env python3
"""
WSGI entry point for the Location Tracker App
Alternative startup method for production deployments
"""

import os
import sys
from app import app

if __name__ == "__main__":
    # Set the port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))
    
    # Run the Flask app
    print(f"🚀 Starting Location Tracker App on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
