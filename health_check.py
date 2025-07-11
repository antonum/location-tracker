#!/usr/bin/env python3
"""
Health check script for Location Tracker App
Tests database connection and basic functionality
"""

import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor

def check_database_connection():
    """Test database connection"""
    try:
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            print("❌ DATABASE_URL environment variable not set")
            return False
        
        print(f"🔍 Testing database connection...")
        print(f"Database URL: {database_url[:50]}...")
        
        conn = psycopg2.connect(database_url, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        
        # Test basic query
        cur.execute("SELECT 1 as test")
        result = cur.fetchone()
        
        if result and result['test'] == 1:
            print("✅ Database connection successful")
            
            # Check if tables exist
            cur.execute("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name IN ('us_states', 'canadian_provinces', 'countries', 'user_records')
            """)
            tables = [row['table_name'] for row in cur.fetchall()]
            
            expected_tables = ['us_states', 'canadian_provinces', 'countries', 'user_records']
            missing_tables = [t for t in expected_tables if t not in tables]
            
            if missing_tables:
                print(f"⚠️  Missing tables: {missing_tables}")
                return False
            else:
                print("✅ All required tables exist")
                return True
        else:
            print("❌ Database query failed")
            return False
            
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

def main():
    """Main health check function"""
    print("🏥 Location Tracker App Health Check")
    print("=" * 40)
    
    # Check environment variables
    required_vars = ['DATABASE_URL']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {missing_vars}")
        return False
    
    # Check database connection
    if not check_database_connection():
        return False
    
    print("✅ All health checks passed!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
