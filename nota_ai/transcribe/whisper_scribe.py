from .base import Transcriber
from typing import Optional
import whisper

class WhisperScriber(Transcriber):
    def __init__(self):
        super().__init__()

    def set_model(self, size="base"):
        self.model = whisper.load_model(size)
        
    def transcribe(self, audio_path: str, prompt: Optional[str] = None):
        text = self.model.transcribe(audio=audio_path, initial_prompt=prompt)
        return text["text"]

