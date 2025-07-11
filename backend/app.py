import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        os.getenv('DATABASE_URL'),
        cursor_factory=RealDictCursor
    )

@app.route('/api/locations', methods=['GET'])
def get_locations():
    """Get all available locations (US states, Canadian provinces, countries)"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Get all locations
        locations = []
        
        # US States
        cur.execute("SELECT name FROM us_states ORDER BY name")
        us_states = [row['name'] for row in cur.fetchall()]
        locations.extend([f"{state}, USA" for state in us_states])
        
        # Canadian Provinces
        cur.execute("SELECT name FROM canadian_provinces ORDER BY name")
        provinces = [row['name'] for row in cur.fetchall()]
        locations.extend([f"{province}, Canada" for province in provinces])
        
        # Other Countries
        cur.execute("SELECT name FROM countries WHERE code NOT IN ('USA', 'CAN') ORDER BY name")
        countries = [row['name'] for row in cur.fetchall()]
        locations.extend(countries)
        
        cur.close()
        conn.close()
        
        return jsonify(locations)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['POST'])
def add_user():
    """Add a new user record"""
    try:
        data = request.get_json()
        name = data.get('name')
        location = data.get('location')
        
        if not name or not location:
            return jsonify({'error': 'Name and location are required'}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute(
            "INSERT INTO user_records (name, location) VALUES (%s, %s) RETURNING id, timestamp",
            (name, location)
        )
        
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            'id': result['id'],
            'name': name,
            'location': location,
            'timestamp': result['timestamp'].isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/recent', methods=['GET'])
def get_recent_users():
    """Get the last 10 user records"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            SELECT id, name, location, timestamp 
            FROM user_records 
            ORDER BY timestamp DESC 
            LIMIT 10
        """)
        
        users = []
        for row in cur.fetchall():
            users.append({
                'id': row['id'],
                'name': row['name'],
                'location': row['location'],
                'timestamp': row['timestamp'].isoformat()
            })
        
        cur.close()
        conn.close()
        
        return jsonify(users)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/stats', methods=['GET'])
def get_user_stats():
    """Get user statistics by location (top 10 + others)"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Get top 10 locations
        cur.execute("""
            SELECT location, COUNT(*) as count 
            FROM user_records 
            GROUP BY location 
            ORDER BY count DESC 
            LIMIT 10
        """)
        
        top_locations = []
        for row in cur.fetchall():
            top_locations.append({
                'location': row['location'],
                'count': row['count']
            })
        
        # Get count of users in locations not in top 10
        if len(top_locations) > 0:
            top_location_names = [loc['location'] for loc in top_locations]
            placeholders = ','.join(['%s'] * len(top_location_names))
            
            cur.execute(f"""
                SELECT COUNT(*) as others_count 
                FROM user_records 
                WHERE location NOT IN ({placeholders})
            """, top_location_names)
            
            others_result = cur.fetchone()
            others_count = others_result['others_count'] if others_result else 0
            
            if others_count > 0:
                top_locations.append({
                    'location': 'Others',
                    'count': others_count
                })
        
        cur.close()
        conn.close()
        
        return jsonify(top_locations)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
