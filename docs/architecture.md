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

## Current Pipeline Milestone

Your pipeline conceptually looks like this:

```
documents
   ↓
loader
   ↓
chunker
   ↓
embedder
```

Each stage transforms the data slightly.

Example flow:

```
example.txt
   ↓
loader
   ↓
{
 text: "...",
 metadata: {source: "example.txt"}
}
   ↓
chunker
   ↓
{
 text: "chunk text",
 metadata: {source: "example.txt", chunk_id: 0}
}
   ↓
embedder
   ↓
{
 embedding: [0.12, 0.44, ...],
 text: "chunk text",
 metadata: {...}
}
```

## Ingestion Pipeline

Raw Documents
→ Load documents
→ Clean text
→ Chunk text
→ Generate embeddings
→ Store vectors + metadata in index