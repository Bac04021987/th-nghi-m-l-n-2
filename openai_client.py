from openai import OpenAI
import os

def get_openrouter_client():
    return OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
