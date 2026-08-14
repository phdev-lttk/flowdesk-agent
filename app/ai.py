import time

from google import genai
from google.genai import errors
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def ask_ai(context: str, question: str) -> str:
    prompt = f"""
Você é um assistente que responde perguntas usando somente o documento fornecido.

REGRAS:
- Responda apenas com informações presentes no documento.
- Não invente informações.
- Se a resposta não estiver no documento, responda:
  "Essa informação não foi encontrada no documento."
- Responda de forma clara e objetiva.

DOCUMENTO:
{context}

PERGUNTA:
{question}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )

            return response.text

        except errors.ServerError:
            if attempt == 2:
                return "O serviço de IA está temporariamente indisponível."

            time.sleep(2 ** attempt)