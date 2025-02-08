from openai import OpenAI
import os
from secret import *


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(question):
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return completion.choices[0].message.content

def request_image(prompt):
    response = client.images.generate(
        model = "dall-e-2",
        prompt = prompt,
        size = "1024x1024",
        quality = "standard",
        n = 1,
    )
    return response.data[0].url