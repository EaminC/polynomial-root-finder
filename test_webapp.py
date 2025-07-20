#!/usr/bin/env python3
"""
Test script for the Polynomial Root Finder Web Application
"""

import requests
import json
import time

def test_webapp():
    """Test the web application functionality"""
    base_url = "http://localhost:5001"
    
    print("🧪 Testing Polynomial Root Finder Web Application")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "name": "x³ - 2x + 1 = 0",
            "coefficients": "1 0 -2 1",
            "expected_roots": 3
        },
        {
            "name": "x² - 4 = 0", 
            "coefficients": "1 0 -4",
            "expected_roots": 2
        },
        {
            "name": "x³ + 1 = 0",
            "coefficients": "1 0 0 1", 
            "expected_roots": 3
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test {i}: {test_case['name']}")
        print(f"   Input: {test_case['coefficients']}")
        
        try:
            # Send request
            response = requests.post(
                f"{base_url}/solve",
                json={"coefficients": test_case['coefficients']},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('success'):
                    print(f"   ✅ Success!")
                    print(f"   📝 Equation: {data['equation']} = 0")
                    print(f"   🎯 Degree: {data['degree']}")
                    print(f"   🔍 Found {len(data['roots'])} roots")
                    
                    # Display roots
                    for root in data['roots']:
                        root_type = "🔴 Real" if root['type'] == 'real' else "🔵 Complex"
                        print(f"      {root_type}: {root['value']}")
                        print(f"         Verification: f({root['value']}) = {root['verification']}")
                    
                    # Check if we found the expected number of roots
                    if len(data['roots']) == test_case['expected_roots']:
                        print(f"   ✅ Correct number of roots found!")
                    else:
                        print(f"   ⚠️  Expected {test_case['expected_roots']} roots, found {len(data['roots'])}")
                        
                else:
                    print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
                    
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Network Error: {e}")
        except Exception as e:
            print(f"   ❌ Unexpected Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing completed!")
    print(f"🌐 Web application is running at: {base_url}")
    print("💡 Open your browser to test the interactive interface!")

if __name__ == "__main__":
    test_webapp() 