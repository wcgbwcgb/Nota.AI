from abc import ABC, abstractmethod

'''
a class used to load audio
'''
class AudioProcessor(ABC):
    def __init__(self):
        self.audio = []
    
    '''
    return: audio file
    '''
    @abstractmethod
    def get_audio(self): 
        pass