from models.gemini_wrapper import query_gemini

def evaluate_answers(text, question, user_answer):
    """
    Evaluates the user's answer for Challenge Me mode.
    """
    prompt = f"""
You are a document-based AI assistant.

Here is an excerpt from the document:
---
{text[:6000]}
---

Question: {question}
User's Answer: {user_answer}

Evaluate the answer. State whether it is correct or partially correct, and explain why based on the document.
"""
    response = query_gemini(prompt)
    return response.strip()