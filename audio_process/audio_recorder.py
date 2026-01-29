from .base import AudioProcessor
from pathlib import Path

class Recorder(AudioProcessor):
    def __init__(self):
        super().__init__()
    
    '''
    return the latest audio
    '''
    def get_audio(self, *args):
        pass

    # override
    def verift_audio(self, file_path):
        pass

    '''
    record real time audio
    '''
    def record(self, duration):
        pass