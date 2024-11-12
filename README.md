# Adapting Whisper for Typical and Atypical (Aphasic) Speech for Singaporean English

## About
This repository holds the code for adapting OpenAI's Whisper model for typical and aphasic English (Singapore) speech.

## The model
You can access the model in HuggingFace [here](https://huggingface.co/f-azm17/whisper-small-singapore-aphasia).

## How to Run

### Step 1: Create a Vast.ai instance

### Step 2: Clone this repository

```
https://github.com/Aphasia-Chatter/aphasia-whisper-fine-tuning.git 
```

Then, `cd` into the repository directory.

### Step 3: Run the script

This script does the following:

- Creates the virtual environment.
- Installs the necessary dependencies and packages.
- Runs the service.

Execute the script by running:

```
chmod +x run.sh
./run.sh
```

You should be able to access the endpoint at:

```
https://<VM_PUBLIC_IP>:8081
```