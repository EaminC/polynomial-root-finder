#!/usr/bin/env python3
"""
Test script for settings functionality
"""

import requests
import json
import time

def test_settings_functionality():
    """Test the settings functionality"""
    base_url = "http://localhost:5001"
    
    print("⚙️ Settings Functionality Test")
    print("=" * 50)
    
    # Test with default parameters
    print("\n📊 Test 1: Default Parameters")
    test_equation = "1 0 -2 1"  # x³ - 2x + 1 = 0
    
    try:
        response = requests.post(
            f"{base_url}/solve",
            json={"coefficients": test_equation},
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Success with default parameters!")
                print(f"   📊 Found {len(data['roots'])} roots")
            else:
                print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test with custom parameters
    print("\n📊 Test 2: Custom Parameters")
    custom_params = {
        "err6": 1e-8,        # Higher precision
        "err": 1e-3,         # Tighter tolerance
        "aberth": 500,       # Fewer iterations
        "chongshumax": 50000,
        "printprecision": 12,
        "range": 100
    }
    
    try:
        response = requests.post(
            f"{base_url}/solve",
            json={
                "coefficients": test_equation,
                "params": custom_params
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Success with custom parameters!")
                print(f"   📊 Found {len(data['roots'])} roots")
                print(f"   ⚙️ Used custom parameters:")
                for key, value in custom_params.items():
                    print(f"      • {key}: {value}")
            else:
                print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test with extreme parameters
    print("\n📊 Test 3: Extreme Parameters")
    extreme_params = {
        "err6": 1e-10,       # Very high precision
        "err": 1e-5,         # Very tight tolerance
        "aberth": 2000,      # Many iterations
        "chongshumax": 100000,
        "printprecision": 15,
        "range": 500
    }
    
    try:
        start_time = time.time()
        response = requests.post(
            f"{base_url}/solve",
            json={
                "coefficients": test_equation,
                "params": extreme_params
            },
            timeout=60
        )
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print(f"   ✅ Success with extreme parameters! ({end_time - start_time:.2f}s)")
                print(f"   📊 Found {len(data['roots'])} roots")
                print(f"   ⚙️ Used extreme parameters:")
                for key, value in extreme_params.items():
                    print(f"      • {key}: {value}")
            else:
                print(f"   ❌ Error: {data.get('error', 'Unknown error')}")
        else:
            print(f"   ❌ HTTP Error: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Settings functionality test completed!")
    print("🌐 Open http://localhost:5001 to test the settings UI!")

def show_settings_features():
    """Show the settings features"""
    print("\n⚙️ Settings Features:")
    print("=" * 30)
    
    features = [
        "🎨 Theme Toggle",
        "   • Light/Dark mode switch",
        "   • Persistent theme preference",
        "   • Smooth transitions",
        "",
        "🔧 Algorithm Parameters",
        "   • Newton-Raphson tolerance (err6)",
        "   • Complex distance tolerance (err)",
        "   • Aberth iteration count",
        "   • Maximum root multiplicity",
        "   • Output precision",
        "   • Initial value range",
        "",
        "💾 Settings Persistence",
        "   • Local storage for preferences",
        "   • Automatic loading on startup",
        "   • Real-time parameter updates",
        "",
        "🔗 GitHub Integration",
        "   • Direct link to repository",
        "   • Open source attribution",
        "",
        "🎯 UI Features",
        "   • Modal settings panel",
        "   • Responsive design",
        "   • Keyboard shortcuts",
        "   • Click outside to close"
    ]
    
    for feature in features:
        print(feature)

if __name__ == "__main__":
    test_settings_functionality()
    show_settings_features() 