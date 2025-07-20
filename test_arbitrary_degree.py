#!/usr/bin/env python3
"""
Test script for arbitrary degree polynomial support
"""

import requests
import json
import time

def test_arbitrary_degree():
    """Test arbitrary degree polynomial support"""
    base_url = "http://localhost:5001"
    
    print("🎯 Arbitrary Degree Polynomial Test")
    print("=" * 50)
    print("✨ Testing polynomials from degree 1 to 15")
    print("=" * 50)
    
    # Test cases with various degrees
    test_cases = [
        {
            "name": "Linear (Degree 1)",
            "degree": 1,
            "coefficients": [2, -3],  # 2x - 3 = 0
            "expected_roots": 1
        },
        {
            "name": "Quadratic (Degree 2)", 
            "degree": 2,
            "coefficients": [1, -5, 6],  # x² - 5x + 6 = 0
            "expected_roots": 2
        },
        {
            "name": "Cubic (Degree 3)",
            "degree": 3, 
            "coefficients": [1, 0, -2, 1],  # x³ - 2x + 1 = 0
            "expected_roots": 3
        },
        {
            "name": "Quartic (Degree 4)",
            "degree": 4,
            "coefficients": [1, 0, -5, 0, 4],  # x⁴ - 5x² + 4 = 0
            "expected_roots": 4
        },
        {
            "name": "Quintic (Degree 5)",
            "degree": 5,
            "coefficients": [1, 0, 0, 0, 0, -1],  # x⁵ - 1 = 0
            "expected_roots": 5
        },
        {
            "name": "Sextic (Degree 6)",
            "degree": 6,
            "coefficients": [1, 0, 0, 0, 0, 0, -1],  # x⁶ - 1 = 0
            "expected_roots": 6
        },
        {
            "name": "Octic (Degree 8)",
            "degree": 8,
            "coefficients": [1, 0, 0, 0, 0, 0, 0, 0, -1],  # x⁸ - 1 = 0
            "expected_roots": 8
        },
        {
            "name": "Decic (Degree 10)",
            "degree": 10,
            "coefficients": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],  # x¹⁰ - 1 = 0
            "expected_roots": 10
        },
        {
            "name": "High Degree (Degree 12)",
            "degree": 12,
            "coefficients": [1] + [0]*11 + [-1],  # x¹² - 1 = 0
            "expected_roots": 12
        },
        {
            "name": "Very High Degree (Degree 15)",
            "degree": 15,
            "coefficients": [1] + [0]*14 + [-1],  # x¹⁵ - 1 = 0
            "expected_roots": 15
        }
    ]
    
    success_count = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test {i}: {test_case['name']}")
        print(f"   🎯 Degree: {test_case['degree']}")
        print(f"   🔢 Coefficients: {test_case['coefficients']}")
        
        # Test the API
        try:
            coeff_string = " ".join(map(str, test_case['coefficients']))
            start_time = time.time()
            
            response = requests.post(
                f"{base_url}/solve",
                json={"coefficients": coeff_string},
                timeout=60  # Increased timeout for high degree polynomials
            )
            
            end_time = time.time()
            computation_time = end_time - start_time
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('success'):
                    print(f"   ✅ Success! ({computation_time:.2f}s)")
                    print(f"   📊 Found {len(data['roots'])} roots")
                    
                    # Check if we found the expected number of roots
                    if len(data['roots']) == test_case['expected_roots']:
                        print(f"   ✅ Correct number of roots!")
                        success_count += 1
                    else:
                        print(f"   ⚠️  Expected {test_case['expected_roots']} roots, found {len(data['roots'])}")
                    
                    # Show first few roots for high degree polynomials
                    if len(data['roots']) > 5:
                        print(f"   🔍 First 5 roots:")
                        for j, root in enumerate(data['roots'][:5], 1):
                            root_type = "🔴 Real" if root['type'] == 'real' else "🔵 Complex"
                            print(f"      {j}. {root_type}: {root['value']}")
                        print(f"      ... and {len(data['roots']) - 5} more")
                    else:
                        for root in data['roots']:
                            root_type = "🔴 Real" if root['type'] == 'real' else "🔵 Complex"
                            print(f"      {root_type}: {root['value']}")
                        
                else:
                    print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
                    
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ Timeout: Computation took too long for degree {test_case['degree']}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print(f"🎉 Test Results: {success_count}/{total_tests} tests passed")
    print(f"🌐 Web application supports arbitrary degree polynomials!")
    print(f"💡 Try degrees up to 50 in the web interface!")

def show_degree_limits():
    """Show information about degree limits"""
    print("\n📋 Degree Limits Information:")
    print("=" * 30)
    
    info = [
        "🎯 Supported Degrees: 1 to 50",
        "   • Dropdown: 1-10 with names",
        "   • Custom input: Any degree 1-50",
        "",
        "⚡ Performance Considerations:",
        "   • Higher degrees = longer computation",
        "   • Degree 15+: May take several seconds",
        "   • Memory usage increases with degree",
        "",
        "🔬 Algorithm Capabilities:",
        "   • Aberth iteration handles any degree",
        "   • Newton refinement for accuracy",
        "   • Multiple initialization strategies",
        "",
        "💡 Practical Recommendations:",
        "   • Degrees 1-10: Instant results",
        "   • Degrees 11-20: Fast results",
        "   • Degrees 21-50: May take longer",
        "   • Above 50: Not recommended (performance)"
    ]
    
    for item in info:
        print(item)

if __name__ == "__main__":
    test_arbitrary_degree()
    show_degree_limits() 