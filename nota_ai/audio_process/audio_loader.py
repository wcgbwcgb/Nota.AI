from .base import AudioProcessor
from pathlib import Path

"""
TODO
1. Implement noise reduction (denoising) options to improve transcription accuracy.(实现降噪的选项)
2. Integrate automatic noise detection within the 'verify_audio' method to suggest preprocessing.(verify()中自动检测是否需要降噪)
"""

class AudioLoader(AudioProcessor):
    """
    Handles audio data ingestion, file integrity verification, and initial preprocessing for the transcription pipeline.
    """
    def __init__(self):
        super().__init__()

    def load(self, *args):
        """
        Verify the existence of input audio files and load them into the pipeline.
        
        Args:
            args: single or multiple audios
        """
        for file in args:
            if not self.verify_audio(file):
                # if loading failed, clear the audio list
                self.audio = []
                raise FileNotFoundError(f"File {file} does not exist")
            self.audio.append(file)
        print(len(args),"files is loaded")

    # override
    def get_audio(self):
        """
        Retrieve the list of successfully loaded audio file paths

        Return:
            a list of audio files
        """
        return self.audio

    # override
    def verify_audio(self, file_path):
        """
        verify if the audio exist
        
        Args:
            file_path: the location of audio file
        """
        path = Path(file_path)
        if not path.exists():
            print(f"file {file_path} does not exist")
            return False
        return True