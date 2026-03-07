import math
import json

# measures how similar two vectors are by looking at the angle between them
# returns a value between -1 (opposite) and 1 (identical direction)
def cosine_similarity(a, b):

    # multiply each pair of numbers together and sum them up (dot product)
    dot_product = sum(x * y for x, y in zip(a, b))

    # calculate the length of each vector
    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    # if either vector has no length, similarity is undefined — return 0
    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    # divide dot product by the product of both lengths to get cosine similarity
    return dot_product / (magnitude_a * magnitude_b)


class VectorIndex:

    def __init__(self):
        # stores all embedded chunks in memory as a flat list
        self.vectors = []

    def add(self, embedded_chunks):
        # add each embedded chunk to the index
        for item in embedded_chunks:
            self.vectors.append(item)

    def search(self, query_embedding, top_k=3):
        results = []

        # compare the query embedding against every stored chunk
        for item in self.vectors:
            score = cosine_similarity(query_embedding, item["embedding"])
            results.append((score, item))

        # sort by similarity score, highest first
        results.sort(key=lambda x: x[0], reverse=True)

        # return only the top_k most similar chunks (without the score)
        return [item for score, item in results[:top_k]]

    def save(self, path):
        # write all vectors to a JSON file so we don't have to rebuild next time
        with open(path, "w") as f:
            json.dump(self.vectors, f)

    def load(self, path):
        # read vectors back from a previously saved JSON file
        with open(path, "r") as f:
            self.vectors = json.load(f)