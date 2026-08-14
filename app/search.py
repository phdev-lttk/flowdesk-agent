from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")


def search_relevant_chunks(
    question: str,
    chunks: list[str],
    top_k: int = 3
) -> list[str]:

    chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
    question_embedding = model.encode(question, convert_to_tensor=True)

    scores = cos_sim(question_embedding, chunk_embeddings)[0]

    top_results = scores.topk(k=min(top_k, len(chunks)))

    relevant_chunks = []

    for index in top_results.indices:
        relevant_chunks.append(chunks[index])

    return relevant_chunks