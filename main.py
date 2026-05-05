import subprocess
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def start_app():

    """Starts the Streamlit application."""
    app_path = os.path.join("src", "ui", "app.py")
    try:
        print("🚀 Starting ClinOps AI Streamlit interface...")
        subprocess.run(["uv", "run", "streamlit", "run", app_path], check=True)
    except KeyboardInterrupt:
        print("\n👋 Shutting down ClinOps AI.")
    except Exception as e:
        print(f"❌ Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_app()
