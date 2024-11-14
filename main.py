from fastapi import FastAPI, File, UploadFile, HTTPException
from model.model import WhisperForSingaporeAphasia
import librosa
from tempfile import NamedTemporaryFile

VALID_AUDIO_TYPES = {
    "audio/wav",
    "audio/x-wav",
    "audio/mpeg",
    "audio/mp4",
    "audio/x-m4a",
    "audio/aac",
    "audio/flac",
    "audio/ogg",
    "audio/x-aiff",
    "audio/wma",
    "audio/wave"
}

app = FastAPI()
model = WhisperForSingaporeAphasia()

@app.post("/transcribe/", status_code=200)
async def transcribe(audiofile: UploadFile = File(...), target_word: str = ""):
    print(audiofile.content_type)
    if audiofile.content_type not in VALID_AUDIO_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Unsupported audio file type. Please upload a valid audio file."
        )
    
    input_prompt = "" if target_word == "" else f"The patient is supposed to say '{target_word}'."
    
    # Writes the content to a temporary file, then load the waveform from there
    try:
        contents = audiofile.file.read()
        temp = NamedTemporaryFile(delete=False)
        with temp as f:
            f.write(contents)
        waveform, _ = librosa.load(temp.name, sr=16000)
    except Exception as e:
        raise HTTPException(
            status_code=415,
            detail=f"Librosa failed to extract audio waveform: {str(e)}"
        )

    try:
        transcription = model.transcribe(waveform, 16000, input_prompt)
    except Exception as e:
        raise HTTPException(
            status_code=415,
            detail=f"Failed to transcribe audio: {str(e)}"
        )

    return {
        "status": "SUCCESS",
        "transcription": transcription
    }