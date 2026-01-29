from nota_ai.transcribe.whisper_scribe import WhisperScriber

transcriber = WhisperScriber()
transcriber.set_model()
text = transcriber.transcribe(audio_path="tests/test_audio1.m4a")
print(text)