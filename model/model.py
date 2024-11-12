import numpy as np
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

class WhisperForSingaporeAphasia:
    def __init__(self):
        self.device = self._get_device()
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained("f-azm17/whisper-small-singapore-aphasia").to(self.device)
        self.processor = AutoProcessor.from_pretrained("f-azm17/whisper-small-singapore-aphasia")
        self.model.eval()
    
    def _get_device(self) -> str:
        if torch.backends.mps.is_available():
            return "mps"
        elif torch.cuda.is_available():
            return "cuda"
        return "cpu"
    
    def transcribe(self, waveform: np.ndarray, sample_rate: int = 16000) -> str:
        inputs = self.processor(waveform, sampling_rate=sample_rate, return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(inputs["input_features"])
        transcription = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return transcription