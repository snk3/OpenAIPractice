from openai import OpenAI
from dotenv import load_dotenv
import os
import config

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
    )

response = client.responses.create(
    model= config.gpt_model,
    input="why do i provide this will upload the data to weaviate as a header?"
)

print(response.output_text)