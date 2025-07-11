#!/usr/bin/env python3
"""
Simple test script to verify the backend API endpoints
"""

import requests
import json
import sys

BASE_URL = "http://localhost:5000/api"

def test_health():
    """Test health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_locations():
    """Test locations endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/locations")
        if response.status_code == 200:
            locations = response.json()
            print(f"✅ Locations endpoint passed ({len(locations)} locations)")
            return True
        else:
            print(f"❌ Locations endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Locations endpoint failed: {e}")
        return False

def test_add_user():
    """Test adding a user"""
    try:
        test_user = {
            "name": "Test User",
            "location": "California, USA"
        }
        response = requests.post(f"{BASE_URL}/users", json=test_user)
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Add user passed (ID: {user_data.get('id')})")
            return True
        else:
            print(f"❌ Add user failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Add user failed: {e}")
        return False

def test_recent_users():
    """Test recent users endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/users/recent")
        if response.status_code == 200:
            users = response.json()
            print(f"✅ Recent users endpoint passed ({len(users)} users)")
            return True
        else:
            print(f"❌ Recent users endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Recent users endpoint failed: {e}")
        return False

def test_user_stats():
    """Test user statistics endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/users/stats")
        if response.status_code == 200:
            stats = response.json()
            print(f"✅ User stats endpoint passed ({len(stats)} locations)")
            return True
        else:
            print(f"❌ User stats endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ User stats endpoint failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Backend API...")
    print("-" * 40)
    
    tests = [
        test_health,
        test_locations,
        test_add_user,
        test_recent_users,
        test_user_stats
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("-" * 40)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
