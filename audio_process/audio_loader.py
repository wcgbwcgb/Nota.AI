from .base import AudioProcessor
from pathlib import Path

class AudioLoader(AudioProcessor):
    def __init__(self):
        super().__init__()

    # override
    def get_audio(self, *args):
        for file in args:
            if not self.verify_audio(file):
                self.audio = []
                raise FileNotFoundError(f"File {file} does not exist")
            self.audio.append(file)
        print(len(args),"files is loaded")
        return self.audio

    # override
    def verift_audio(self, file_path):
        path = Path(file_path)
        if not path.exists():
            print(f"file {file_path} does not exist")
            return False
        return True