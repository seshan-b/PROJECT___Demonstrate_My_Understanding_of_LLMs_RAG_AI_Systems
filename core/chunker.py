# takes a list of documents and splits each one into smaller chunks
# chunk_size: how many words per chunk
# overlap: how many words to repeat from the previous chunk so we don't lose context at the edges
def chunk_documents(documents, chunk_size=100, overlap=20):
    chunks = []

    for doc in documents:
        text = doc["text"]
        metadata = doc["metadata"]

        # break the text into a list of words
        words = text.split()

        # slide through the words, moving forward by (chunk_size - overlap) each time
        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)

            chunk = {
                "text": chunk_text,
                "metadata": metadata  # keep track of where this chunk came from
            }

            chunks.append(chunk)

    return chunks