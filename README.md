# Facerecog
The Real-Time Face Recognition System for Attendance Tracking is a Python-based application designed to streamline and automate attendance logging using facial recognition technology. This project detects and recognizes human faces through a live camera feed and records attendance in real-time, minimizing manual entry and reducing errors.
It is especially useful in:
-  Educational institutions: Automate classroom attendance
-  Workplaces: Track employee check-ins without ID cards or biometrics
-  Research projects: Study real-time recognition workflows
-  Restricted access areas: Enable secure identity verification
Built using OpenCV, dlib, and Python 3.12, it supports both online and offline setups with a precompiled .whl file to install dlib easily.
How to Set Up and Run the Project
Step 1: Check Python version
    - Make sure you're using Python 3.12
    - python --version
      
STEP 2: Create a virtual environment
    - python -m venv env      # Create virtual environment
    - cd env\Scripts          # Go into Scripts folder
    - activate                # Activate the virtual environment
  # For macOS/Linux users: source env/bin/activate
  
STEP 3: Install dependencies    
    - pip install path\to\dlib‑19.XX.XX‑cp312‑cp312‑win_amd64.whl        # First install dlib from the precompiled .whl file (offline setup).
    - pip install -r requirements.txt
    
STEP 4: Run the application
    - cd path\to\facerecog      # Navigate to the root folder if you're not already there.
    - python facerecog.py       # Run the face recognition script.
