import os
import numpy as np

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_embedding(text: str) -> np.ndarray:
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return np.array(
        response.embeddings[0].values,
        dtype=np.float32
    )


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def search_relevant_chunks(
    question: str,
    chunks: list[str],
    top_k: int = 3
) -> list[str]:

    question_embedding = get_embedding(question)

    results = []

    for chunk in chunks:
        chunk_embedding = get_embedding(chunk)

        score = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        results.append((score, chunk))

    results.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        chunk
        for _, chunk in results[:top_k]
    ]
