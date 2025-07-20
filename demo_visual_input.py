#!/usr/bin/env python3
"""
Demo script for the new visual input interface
"""

import requests
import json
import time

def demo_visual_input():
    """Demonstrate the new visual input interface"""
    base_url = "http://localhost:5001"
    
    print("🎨 Visual Input Interface Demo")
    print("=" * 50)
    print("✨ New Features:")
    print("   • Select polynomial degree from dropdown")
    print("   • Individual coefficient input fields")
    print("   • Real-time equation preview")
    print("   • Visual feedback and validation")
    print("=" * 50)
    
    # Test cases with different degrees
    test_cases = [
        {
            "name": "Linear Equation (Degree 1)",
            "degree": 1,
            "coefficients": [2, -3],  # 2x - 3 = 0
            "description": "Simple linear equation"
        },
        {
            "name": "Quadratic Equation (Degree 2)", 
            "degree": 2,
            "coefficients": [1, -5, 6],  # x² - 5x + 6 = 0
            "description": "Classic quadratic with real roots"
        },
        {
            "name": "Cubic Equation (Degree 3)",
            "degree": 3, 
            "coefficients": [1, 0, -2, 1],  # x³ - 2x + 1 = 0
            "description": "Cubic with interesting roots"
        },
        {
            "name": "Quartic Equation (Degree 4)",
            "degree": 4,
            "coefficients": [1, 0, -5, 0, 4],  # x⁴ - 5x² + 4 = 0
            "description": "Quartic with multiple real roots"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test {i}: {test_case['name']}")
        print(f"   📝 {test_case['description']}")
        print(f"   🎯 Degree: {test_case['degree']}")
        print(f"   🔢 Coefficients: {test_case['coefficients']}")
        
        # Simulate the visual input process
        print(f"   🖱️  Visual Input Process:")
        print(f"      1. Select degree {test_case['degree']} from dropdown")
        print(f"      2. Input coefficients in individual fields:")
        
        for j, coeff in enumerate(test_case['coefficients']):
            power = test_case['degree'] - j
            if power == 0:
                term = "constant"
            elif power == 1:
                term = "x"
            else:
                term = f"x^{power}"
            print(f"         • {term}: {coeff}")
        
        # Test the API
        try:
            coeff_string = " ".join(map(str, test_case['coefficients']))
            response = requests.post(
                f"{base_url}/solve",
                json={"coefficients": coeff_string},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get('success'):
                    print(f"   ✅ Success!")
                    print(f"   📊 Found {len(data['roots'])} roots")
                    
                    # Show roots
                    for root in data['roots']:
                        root_type = "🔴 Real" if root['type'] == 'real' else "🔵 Complex"
                        print(f"      {root_type}: {root['value']}")
                        
                else:
                    print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
                    
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Demo completed!")
    print(f"🌐 Open http://localhost:5001 to try the new interface!")
    print("\n💡 How to use the new interface:")
    print("   1. Select polynomial degree from dropdown")
    print("   2. Enter coefficients in individual input fields")
    print("   3. Watch the equation preview update in real-time")
    print("   4. Click 'Find All Roots' to solve")
    print("   5. Try the quick examples for instant setup")

def show_interface_features():
    """Show the key features of the new interface"""
    print("\n🎨 Interface Features:")
    print("=" * 30)
    
    features = [
        "📋 Degree Selection Dropdown",
        "   • Choose from 1-10 degree polynomials",
        "   • Clear labels (Linear, Quadratic, etc.)",
        "   • Automatic coefficient field generation",
        "",
        "🔢 Individual Coefficient Inputs",
        "   • Separate input field for each term",
        "   • Clear labels (x, x², x³, etc.)",
        "   • Number input with decimal support",
        "   • Hover effects and visual feedback",
        "",
        "👁️ Real-time Equation Preview",
        "   • Live equation display as you type",
        "   • Proper mathematical formatting",
        "   • Handles zero coefficients gracefully",
        "   • Shows simplified form",
        "",
        "✅ Smart Validation",
        "   • Prevents all-zero coefficient equations",
        "   • Disables solve button until valid input",
        "   • Clear error messages",
        "   • Visual state indicators",
        "",
        "🎯 Quick Examples",
        "   • One-click preset equations",
        "   • Auto-fills degree and coefficients",
        "   • Perfect for testing and learning"
    ]
    
    for feature in features:
        print(feature)

if __name__ == "__main__":
    demo_visual_input()
    show_interface_features() 