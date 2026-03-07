# mock LLM — no API connection
# simulates what a real LLM would receive and return
# swap this out for a real API call when ready
def generate_answer(prompt):

    # echo back the prompt so we can verify the pipeline is passing data correctly
    return f"[MOCK LLM RESPONSE]\n\nReceived prompt:\n\n{prompt}"