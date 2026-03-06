# Architecture

## RAG Pipeline Flow

User asks a question
→ system converts question into an embedding
→ system searches indexed document embeddings
→ system selects top matching chunks
→ system builds a prompt with context
→ LLM generates final answer

## Query Pipeline

User Query
→ Chunk query if needed
→ Convert query to embedding
→ Search vector index
→ Retrieve top-k chunks
→ Build prompt
→ Send to LLM
→ Return answer

## Ingestion Pipeline

Raw Documents
→ Load documents
→ Clean text
→ Chunk text
→ Generate embeddings
→ Store vectors + metadata in index