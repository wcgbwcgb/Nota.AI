from nota_ai.engine import NotaEngine

engine = NotaEngine(api_key="your-api-key")

print(engine.run(audio_path="tests/test_audio1.m4a"))