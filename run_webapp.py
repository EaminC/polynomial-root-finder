#!/usr/bin/env python3
"""
Polynomial Root Finder Web Application
A beautiful, interactive web app for solving polynomial equations
"""

import os
import sys
import webbrowser
import threading
import time
from app import app

def open_browser():
    """Open browser after a short delay"""
    time.sleep(1.5)
    webbrowser.open('http://localhost:5001')

def main():
    print("🚀 Starting Polynomial Root Finder Web Application...")
    print("=" * 60)
    print("📊 Features:")
    print("   • Interactive polynomial equation solver")
    print("   • Complex root support with Aberth+Newton method")
    print("   • Beautiful, responsive web interface")
    print("   • Real-time plotting with Plotly")
    print("   • Mobile-friendly design")
    print("=" * 60)
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    print("🌐 Opening web browser...")
    print("📱 Access the app at: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        # Run the Flask app
        app.run(
            host='0.0.0.0',
            port=5001,
            debug=False,
            use_reloader=False
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        print("Thanks for using Polynomial Root Finder!")

if __name__ == '__main__':
    main() 