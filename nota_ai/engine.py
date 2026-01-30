from nota_ai.audio_process.audio_loader import AudioLoader
from nota_ai.transcribe.whisper_scribe import WhisperScriber
from nota_ai.generate.llm_generator import LLMGenerator

"""
TODO
1. IMPORTANT: Implement 'Real-time Synthesis' to enable live note generation during active recording sessions.
2. Develop a robust 'CLI (Command Line Interface)' for developer-friendly local execution
3. Support 'Multi-format Exporting' beyond Markdown, including PDF, HTML, and LaTeX for academic submission.
4. Design a 'User-Centric Interface' (GUI or Web-based) to improve accessibility for non-technical students
5. Integrate 'Advanced Configuration Management' using .env or YAML files to separate secrets from code.
"""

class NotaEngine():
    """
    The core orchestrator of the Nota.AI pipeline, integrating audio transcription and LLM-based note generation into a seamless workflow.
    """
    def __init__(self, scribe_model_size="base", provider="deepseek", api_key=None):
        """
        Initializes the engine with specific transcription and generation configurations
        
        Args:
            scribe_model_size: Model size for the Whisper transcriber
            provider: LLM service provider
            api_key: Secret key for the LLM API
        """
        self.audio_loader = AudioLoader()
        self.transcriber = WhisperScriber(size=scribe_model_size)
        self.generator = LLMGenerator()
        if api_key:
            self.generator.set_client(provider=provider, api_key=api_key)

    def run(self, audio_path):
        """
        Execute the full pipeline: Audio -> Transcript -> Structured Notes
        
        Args:
            audio_path: Path to the source audio file
            
        Returns:
            str: The final synthesized Markdown notes
        """
        text = ""  # transcript text

        # load and verification
        self.audio_loader.load(audio_path)
        audio_list = self.audio_loader.get_audio()

        # transcribe
        for audio in audio_list:
            text += self.transcriber.transcribe(audio) + "\n"

        # generate
        note = self.generator.generate(text)
        return note