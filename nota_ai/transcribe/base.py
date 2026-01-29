from abc import ABC, abstractmethod

'''
an abstract class used to transform audio into text
'''
class Transcriber(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def transcribe(self):
        pass

    @abstractmethod
    def set_model(self):
        pass