from abc import ABC, abstractmethod

'''
an abstract class used to transform audio into text
'''
class Transcriber(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def transcribe():
        pass