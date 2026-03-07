# takes the user's query and the retrieved chunks, and assembles them into a prompt
# the prompt tells the LLM what context to use when answering the question
def build_prompt(query, retrieved_chunks):

    # pull just the text out of each chunk and join them together as the context block
    context_parts = [chunk["text"] for chunk in retrieved_chunks]
    context = "\n\n".join(context_parts)

    # build the final prompt with clear sections for context and the question
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:"""

    return prompt