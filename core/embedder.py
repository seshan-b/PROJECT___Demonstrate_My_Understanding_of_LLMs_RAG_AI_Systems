import random


# embed a single query string and return just the embedding vector
def embed_query(text):
    return [random.random() for _ in range(10)]


def generate_embeddings(chunks):

    embedded_chunks = []

    for chunk in chunks:

        embedding = [random.random() for _ in range(10)]

        embedded_chunk = {
            "embedding": embedding,
            "text": chunk["text"],
            "metadata": chunk["metadata"]
        }

        embedded_chunks.append(embedded_chunk)

    return embedded_chunks