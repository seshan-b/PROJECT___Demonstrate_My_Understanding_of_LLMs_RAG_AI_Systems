# the retriever sits between the vector index and the rest of the pipeline
# it takes a query embedding, finds the most relevant chunks, and returns them
class Retriever:

    def __init__(self, vector_index):
        # holds a reference to the vector index so we can search it
        self.vector_index = vector_index

    def retrieve(self, query_embedding, top_k=3):
        # ask the index to find the top_k most similar chunks to the query
        results = self.vector_index.search(query_embedding, top_k=top_k)

        # return only the text and metadata — this is what the prompt builder needs
        return [
            {
                "text": item["text"],
                "metadata": item["metadata"]
            }
            for item in results
        ]