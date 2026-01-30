from .base import Transcriber
from typing import Optional
import whisper

"""
TODO
1. Hardware detection
2. progess callback(进度条)
3. Audio Chunking(if needed)
"""

class WhisperScriber(Transcriber):
    """
    WhisperScriber is a transcribe tool by using Whisper
    """
    def __init__(self, size="base"):
        """
        Initializes the transcriber with a specific model size.
        
        Args:
            model_size: The size of the Whisper model to load.
        """
        super().__init__()
        self.model = whisper.load_model(size)
        
    def transcribe(self, audio_path: str, prompt: Optional[str] = None):
        """
        Transcribe audio to text with an optional initial prompt for context.
        
        Args:
            audio_path: Path to the target audio file.
            prompt: Optional text to guide the model's style/vocabulary.
            
        Returns:
            The transcribed text content.
        """
        text = self.model.transcribe(audio=audio_path, initial_prompt=prompt)
        return text["text"]

