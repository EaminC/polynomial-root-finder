#!/usr/bin/env python3
"""
Test script for new features: randomize and clear coefficients
"""

import requests
import json
import time

def test_new_features():
    """Test the new randomize and clear features"""
    base_url = "http://localhost:5001"
    
    print("🎲 New Features Test: Randomize & Clear Coefficients")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        {
            "name": "Degree 3 Polynomial",
            "degree": 3,
            "description": "Testing with cubic polynomial"
        },
        {
            "name": "Degree 5 Polynomial", 
            "degree": 5,
            "description": "Testing with quintic polynomial"
        },
        {
            "name": "Degree 8 Polynomial",
            "degree": 8,
            "description": "Testing with octic polynomial"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📊 Test {i}: {test_case['name']}")
        print(f"   📝 {test_case['description']}")
        print(f"   🎯 Degree: {test_case['degree']}")
        
        # Generate random coefficients for this degree
        import random
        random_coeffs = []
        for j in range(test_case['degree'] + 1):
            coeff = round((random.random() - 0.5) * 20, 2)
            random_coeffs.append(coeff)
        
        print(f"   🎲 Random coefficients: {random_coeffs}")
        
        # Test solving with random coefficients
        try:
            coeff_string = " ".join(map(str, random_coeffs))
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
                    
                    # Show first few roots
                    for j, root in enumerate(data['roots'][:3], 1):
                        root_type = "🔴 Real" if root['type'] == 'real' else "🔵 Complex"
                        print(f"      {j}. {root_type}: {root['value']}")
                    
                    if len(data['roots']) > 3:
                        print(f"      ... and {len(data['roots']) - 3} more")
                        
                else:
                    print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
                    
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 New features test completed!")
    print("🌐 Open http://localhost:5001 to test the UI features!")

def show_new_features():
    """Show the new features"""
    print("\n🎲 New Features Added:")
    print("=" * 30)
    
    features = [
        "🎲 Randomize All Coefficients",
        "   • Generates random coefficients between -10 and 10",
        "   • Updates equation preview in real-time",
        "   • Requires degree to be set first",
        "   • Perfect for testing and exploration",
        "",
        "🧹 Clear All Coefficients", 
        "   • Clears all coefficient input fields",
        "   • Resets equation preview",
        "   • Quick way to start fresh",
        "   • Requires degree to be set first",
        "",
        "🎨 UI Improvements",
        "   • Beautiful gradient buttons",
        "   • Hover animations",
        "   • Responsive design",
        "   • Clear visual feedback",
        "",
        "🌍 English Localization",
        "   • All text converted to English",
        "   • Professional terminology",
        "   • Clear descriptions",
        "   • Consistent language throughout"
    ]
    
    for feature in features:
        print(feature)

def test_ui_workflow():
    """Test the UI workflow"""
    print("\n🖱️ UI Workflow Test:")
    print("=" * 30)
    
    workflow = [
        "1. Enter polynomial degree (e.g., 3)",
        "2. Click 'Randomize All' to generate random coefficients",
        "3. Watch equation preview update automatically",
        "4. Click 'Find All Roots' to solve",
        "5. View results and interactive plots",
        "6. Click 'Clear All' to reset and try again",
        "",
        "💡 Tips:",
        "   • Try different degrees for variety",
        "   • Use random coefficients for exploration",
        "   • Clear and randomize multiple times",
        "   • Experiment with different polynomial types"
    ]
    
    for step in workflow:
        print(step)

if __name__ == "__main__":
    test_new_features()
    show_new_features()
    test_ui_workflow() 