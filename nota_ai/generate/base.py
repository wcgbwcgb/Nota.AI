from abc import ABC, abstractmethod

'''
a class used to generate notes
'''
class Generator(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def generate():
        pass