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
    
    def transcribe(self, waveform: np.ndarray, sample_rate: int = 16000, input_prompt: str = "") -> str:
        inputs = self.processor(waveform, sampling_rate=sample_rate, return_tensors="pt").to(self.device)
        input_prompt_ids = self.processor.tokenizer(input_prompt, return_tensors="pt").input_ids.squeeze().to(self.device)
        with torch.no_grad():
            if input_prompt == "":
                generated_ids = self.model.generate(
                    input_features=inputs["input_features"], 
                    temperature=0.0
                )
            else:
                generated_ids = self.model.generate(
                    input_features=inputs["input_features"], 
                    prompt_ids=input_prompt_ids,
                    temperature=0.0
                )
        transcription = self.processor.batch_decode(generated_ids, skip_special_tokens=True)
        return transcription[0]