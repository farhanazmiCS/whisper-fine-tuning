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

# Prompt the user to enter their Hugging Face token
read -sp "Enter your Hugging Face token: " HF_TOKEN
echo # for a new line after the token input

# Use the entered token to log in to Hugging Face
huggingface-cli login --token "$HF_TOKEN"

# Get the public IP and output the access URL
PUBLIC_IP=$(curl -s ifconfig.me)
echo "Your FastAPI app is running at: http://$PUBLIC_IP:50001"

# Run the application
uvicorn main:app --host 0.0.0.0 --port 50001