# Architecture

## RAG Pipeline Flow

User asks a question
→ system converts question into an embedding
→ system searches indexed document embeddings
→ system selects top matching chunks
→ system builds a prompt with context
→ LLM generates final answer