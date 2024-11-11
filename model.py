from transformers import AutoModelForSpeechSeq2Seq, WhisperProcessor
import numpy as np
import torch

class WhisperForSingaporeAphasia:
    def __init__(self):
        self.device = self._get_device()
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained("f-azm17/whisper-small-singapore-aphasia").to(self.device)
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-small.en")
    
    def _get_device(self) -> str:
        if torch.backends.mps.is_available():
            return "mps"
        elif torch.cuda.is_available():
            return "cuda"
        return "cpu"
    
    def transcribe(self, waveform_path: str = '', sample_rate: int = 16000) -> str:
        try:
            waveform = np.load(waveform_path)
        except:
            raise OSError
        inputs = self.processor(waveform, sampling_rate=sample_rate, return_tensors="pt").to(self.device)
        with torch.no_grad():
            generated_ids = self.model.generate(inputs["input_features"])
        transcription = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return transcription