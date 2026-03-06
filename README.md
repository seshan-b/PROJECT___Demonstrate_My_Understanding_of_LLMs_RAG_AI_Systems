# Demonstrate My Understanding of LLMs, RAG & AI Systems

I am building a mini RAG AI system that takes a user query, converts it into embeddings, retrieves relevant documents using vector search, and returns an answer through an LLM.

## Project Structure

```
├── app/
│   ├── main.py
│   ├── config.py
│   └── schemas.py
│
├── core/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_index.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── llm.py
│
├── data/
│   └── raw/
│
├── docs/
│   └── architecture.md
│
├── tests/
│
├── requirements.txt
├── .env
└── README.md
```