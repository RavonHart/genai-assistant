from models.gemini_wrapper import query_gemini
import re
def handle_question(text, question, chat_history=None):
    # Build memory context
    context = ""
    if chat_history:
        context = "\n".join(
            [f"Q: {entry['question']}\nA: {entry['answer']}" for entry in chat_history[-3:]]
        )

    prompt = f"""
You are a document-aware assistant.

Here is the current document:
{text[:6000]}

Here is the previous conversation (if any):
{context}

Now answer the user's new question and provide a supporting snippet from the document.

Question: {question}

Return in this format:
Answer: ...
Snippet: ...
"""
    response = query_gemini(prompt)

    try:
        answer = response.split("Snippet:")[0].replace("Answer:", "").strip()
        snippet = response.split("Snippet:")[1].strip()
    except:
        answer = response.strip()
        snippet = "⚠️ Snippet could not be extracted."

    return answer, snippet


def generate_challenges(text):
    prompt = f"""
Create exactly 3 logic- or reasoning-based questions based on the document below.
Each question should be clearly numbered (1., 2., 3.) and start on a new line.

Document:
{text[:6000]}
"""

    response = query_gemini(prompt)

    # Clean and split based on numbered lines (1. 2. 3.)
    raw = response.strip()
    matches = re.findall(r"(?:\d[\.\)]\s+)(.*?)(?=(?:\n\d[\.\)]|\Z))", raw, re.DOTALL)

    # Strip whitespace and ensure they are real questions (not titles or headers)
    questions = [q.strip() for q in matches if "?" in q]

    return questions[:3]