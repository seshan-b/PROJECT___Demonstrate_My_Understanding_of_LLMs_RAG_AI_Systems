import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.loader import load_documents
from core.chunker import chunk_documents
from core.embedder import generate_embeddings, embed_query
from core.vector_index import VectorIndex
from core.retriever import Retriever
from core.prompt_builder import build_prompt
from core.llm import generate_answer

# load documents from the raw/ directory
documents = load_documents("data/raw")

# split them into manageable chunks
chunks = chunk_documents(documents)

# create embeddings for each chunk
embedded_chunks = generate_embeddings(chunks)

# build a vector index for fast similarity search
vector_index = VectorIndex()
vector_index.add(embedded_chunks)

# create a retriever that uses the index
retriever = Retriever(vector_index)

# example query
query = "What is the capital of France?"

# embed the query
query_embedding = embed_query(query)

# retrieve relevant chunks
retrieved_chunks = retriever.retrieve(query_embedding, top_k=3)

# build a prompt with the context and question
prompt = build_prompt(query, retrieved_chunks)

# generate an answer using the LLM
answer = generate_answer(prompt)

print(answer)