from .base import AudioProcessor
from pathlib import Path

'''
TODO
1. Implement a 'Device' class to manage input device selection for the record() method.
2. Complete the core logic for audio capturing and validation.
'''

class Recorder(AudioProcessor):
    """
    Handles live audio recording, device management, and initial verification of the captured streams
    """
    def __init__(self):
        super().__init__()
    
    def get_audio(self):
        """
        Provide access to recorded audio
        """
        pass

    # override
    def _verift_audio(self, file_path):
        """
        verify if a file exist and available
        
        :param file_path: location of file that need to be verified
        """
        pass

    def record(self, duration):
        """
        Record real-time audio from all kind of devices
        
        :param duration: recording time of a audio file
        """
        pass