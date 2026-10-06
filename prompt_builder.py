"""
prompt_builder.py

Builds the final prompt sent to Gemini.
"""


def build_prompt(system_prompt, conversation_history, retrieved_chunks, user_query):
    """
    Combines the system prompt, conversation history,
    retrieved context and the current user question.

    Args:
        system_prompt (str)
        conversation_history (str)
        retrieved_chunks (list[str])
        user_query (str)

    Returns:
        str
    """

    # Combine all retrieved chunks into one block of text
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
{system_prompt}

Conversation History:

{conversation_history}

Relevant Context:

{context}

User:
{user_query}
"""

    return prompt