# Demonstrate My Understanding of LLMs, RAG & AI Systems

I am building a mini RAG AI system that takes a user query, converts it into embeddings, retrieves relevant documents using vector search, and returns an answer through an LLM.

## How Chunking Works

Modern LLM systems instead do:

```
Document
   ↓
Split into chunks
   ↓
Embed each chunk
```

Example:

```
example.txt (2000 words)

↓ chunker

chunk_0
chunk_1
chunk_2
chunk_3
```

Each chunk becomes its own embedding.

## The Math Behind Vectors

### 1. Two vectors in space

Imagine two vectors starting from the origin.

```
        B
       /
      /
     /
    /
   /
  O-------- A
```

- O = origin (0,0)
- A = vector A
- B = vector B
- The angle between them = θ

Cosine similarity measures that angle.

### 2. The math

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

Where:

```
A · B     = dot product
||A||     = magnitude of vector A
||B||     = magnitude of vector B
```

### 3. Dot product visual

If we have:

```
A = [2,3]
B = [4,1]
```

Dot product:

```
A · B = (2×4) + (3×1)
      = 8 + 3
      = 11
```

### 4. Vector magnitude

Magnitude = vector length.

```
||A|| = √(2² + 3²)
      = √13

||B|| = √(4² + 1²)
      = √17
```

### 5. Final cosine similarity

```
cos(θ) = 11 / ( √13 × √17 )
```

Result will be between -1 and 1.

```
1   → same direction
0   → unrelated
-1  → opposite direction
```

### 6. Why this works for AI

Embeddings represent semantic meaning.

Example conceptually:

```
"dog" vector
"puppy" vector
```

Their vectors point in similar directions → cosine similarity ≈ 0.9

But:

```
"dog"
"airplane"
```

Vectors point in very different directions → cosine similarity ≈ 0.1

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