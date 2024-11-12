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

# Prompt for Hugging Face token
read -sp "Enter your Hugging Face token: " HUGGING_FACE_TOKEN
echo
echo $HUGGING_FACE_TOKEN | huggingface-cli login --token

# Run the application
uvicorn main:app --host 0.0.0.0 --port 8081

# Get the public IP and output the access URL
PUBLIC_IP=$(curl -s ifconfig.me)
echo "Your FastAPI app is running at: http://$PUBLIC_IP:8081"