from .base import Generator
from openai import OpenAI

class LLMGenerator(Generator):
    def __init__(self):
        super().__init__()
        self.model_name = None
        self.system_instruction = """
            You are a polymath academic assistant. Your goal is to transform a lecture transcript into structured notes.
            
            1. **Denoise**: Remove stutters, filler words, and administrative chatter.
            2. **Classify**: Adapt structure for STEM (Logic/Equations) or Humanities (Narrative/Context).
            3. **Format**: Use Markdown. Use LaTeX for ANY mathematical expression.
            
            # [Dynamic Title]
            ## 1. Executive Summary
            ## 2. Core Taxonomy
            ## 3. Formalisms / Key Quotes
            ## 4. Review & Action Items
            """

    '''
    return a client
    '''
    def set_client(self, provider: str, api_key):
        configs = {
            "openai": {
                "api_key": api_key,
                "base_url": "https://api.openai.com/v1"
            },
            "deepseek": {
                "api_key": api_key,
                "base_url": "https://api.deepseek.com"
            }
        }

        config = configs.get(provider.lower())
        self.model_name = provider.lower()
        if not config:
            raise ValueError(f"Unsupported provider: {provider}")

        self.client = OpenAI(
            api_key=config["api_key"],
            base_url=config["base_url"]
        )
    
    # override
    def generate(self, raw_text, model="deepseek-chat"):
        if not self.client:
            raise RuntimeError("Please call set_client() before generate().")
        if self.model_name == "openai":
            response = self.client.responses.create(
                model=model,
                instructions=self.system_instruction,
                input=raw_text,
            )
            return response.output_text
        else:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": self.system_instruction},
                    {"role": "user", "content": raw_text},
                ],
                stream=False
            )
            return response.choices[0].message.content
        