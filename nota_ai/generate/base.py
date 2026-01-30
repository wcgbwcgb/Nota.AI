from abc import ABC, abstractmethod

'''
a class used to generate notes
'''
class Generator(ABC):
    def __init__(self):
        self.client = None

    @abstractmethod
    def generate(self):
        pass