#!/usr/bin/env python3
"""
Streamlit app wrapper for Vercel deployment
Exposes Streamlit via HTTP on serverless functions
"""
import subprocess
import sys
import os

# Install streamlit and dependencies
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

# Run the Streamlit app
os.system("streamlit run app.py --server.port=3000 --server.address=0.0.0.0 --server.headless=true")
