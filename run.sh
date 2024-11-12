#!/bin/bash

# Update package list
sudo apt update -y

# Install ffmpeg backend
sudo apt-get -y install ffmpeg

# Setup virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --host 0.0.0.0 --port 8081