from nota_ai.audio_process.audio_loader import AudioLoader
from nota_ai.transcribe.whisper_scribe import WhisperScriber
from nota_ai.generate.llm_generator import LLMGenerator

class NotaEngine():
    def __init__(self, scribe_model_size="base", provider="deepseek", api_key=None):
        self.transcriber = WhisperScriber()
        self.transcriber.set_model(size=scribe_model_size)
        self.generator = LLMGenerator()
        if api_key:
            self.generator.set_client(provider=provider, api_key=api_key)
        
        if api_key:
            self.generator.set_client(provider, api_key)

    def run(self, audio_path):
        text = self.transcriber.transcribe(audio_path)
        note = self.generator.generate(text)
        return note