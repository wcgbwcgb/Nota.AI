from abc import ABC, abstractmethod

'''
a class used to process audio
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

    '''
    return: if the audio exist, return true
    '''
    @abstractmethod
    def verify_audio(self): 
        pass