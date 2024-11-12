# Adapting Whisper for Typical and Atypical (Aphasic) Speech for Singaporean English

## About
This repository holds the code for adapting OpenAI's Whisper model for typical and aphasic English (Singapore) speech.

## The model
You can access the model in HuggingFace [here](https://huggingface.co/f-azm17/whisper-small-singapore-aphasia).

## How to Run

### Step 1: Create a Vast.ai instance

#### 1.1 Instance Template

Click this [link](https://cloud.vast.ai/?ref_id=139955&template_id=8ac2e196e326f60dbbaddd030a39bfcf) to create the instance with the custom template. By default, Vast.ai only creates one exposed port for the docker container.

#### 1.2 Rent a GPU

Create a GPU instance by clicking the 'RENT' button in any GPU. To reduce latency as much as possible, click **Planet Earth** in the dropdown and select **Asia**.

#### 1.3 Enter the Instance

Take a look at your opened instances by clicking the **Instances** button on the left side. It will take some time for your instance to get up and running. Once it starts running, you should be able to see the **Open** button turn blue.

### Step 2: Clone this repository

#### 2.1 Clone the repository

Once you have entered the instance, open the terminal. You can do this by clicking `file -> new -> terminal`. When you're in the terminal, run this:

```
git clone https://github.com/Aphasia-Chatter/aphasia-whisper-fine-tuning.git 
```

Then, run this:

```
cd aphasia-whisper-fine-tuning
```

### Step 3: Run the script

This script does the following:

- Creates the virtual environment.
- Installs the necessary dependencies and packages.
- Runs the service.

#### 3.1 Enable permissions to execute scripts

Run:

```
chmod +x run.sh
```

#### 3.2 Run the script

Run:

```
./run.sh
```

#### 3.3 Enter Hugging Face Credentials

You will be prompted to enter the Hugging Face credentials to gain access to the model. Consult Farhan for details.

### Step 4: Use the API

The application will run on port `50001`. In your Vast.ai instance, you can see which external port is mapped to the internal port `50001` by clicking over the public IP of your running instance. Once you click it, you can see something like this:

```
Open Ports

172.81.127.5:63678 -> 22/tcp
172.81.127.5:63952 -> 50001/tcp
<PUBLIC IP>:<EXTERNAL_PORT> -> <INTERNAL_IP>/tcp

```

As you can see, external port `63952` is mapped to internal port `50001`, which is what our application is running on. This is just an example, as external port and public IPs can change. So, you can access the endpoint at:

```
https://<PUBLIC_IP>:<EXTERNAL_PORT_THAT_MAPS_TO_INTERNAL_PORT_50001>
```

Use these parameters to transcribe:

Request Type: `POST`

Request Endpoint:

```
https://<PUBLIC_IP>:<EXTERNAL_PORT_THAT_MAPS_TO_INTERNAL_PORT_50001>/transcribe
```

Request Headers:

```
Accept: */*
Content-Type: multipart/form-data
```

Request Body:

```
audiofile: <Audio File (.m4a, .wav, etc.)>
```

Expected Response:

```
{
	"status": "SUCCESS",
	"transcription": "! I don't know how to smile, Smiling Face, I think."
}
```