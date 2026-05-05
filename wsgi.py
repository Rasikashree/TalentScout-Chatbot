"""
WSGI wrapper for Streamlit on Vercel
This allows Streamlit to run as a web service on Vercel
"""
import sys
import os
from pathlib import Path

# Add the project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set environment variables for Streamlit
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_PORT"] = "3000"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

# Import and run Streamlit app
from streamlit.web import cli as stcli

def app(environ, start_response):
    """WSGI application for Vercel"""
    stcli.main(["run", "app.py", "--server.port=3000", "--server.address=0.0.0.0", "--server.headless=true"])
    
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"Streamlit app is running"]

if __name__ == "__main__":
    # For local testing
    import streamlit.cli as cli
    cli.main()
