"""
memory.py

Helper functions for managing conversation history.
"""


def add_user_message(conversation, message):
    """
    Adds the user's message to the conversation history.

    Args:
        conversation (list): Conversation history.
        message (str): User's message.
    """

    conversation.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(conversation, message):
    """
    Adds the assistant's response to the conversation history.

    Args:
        conversation (list): Conversation history.
        message (str): Assistant's response.
    """

    conversation.append({
        "role": "assistant",
        "content": message
    })


def get_history(conversation):
    """
    Converts the conversation history into a single string.

    Args:
        conversation (list): Conversation history.

    Returns:
        str
    """

    history = ""

    for message in conversation:

        history += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    return history


def clear_memory(conversation):
    """
    Clears the conversation history.

    Args:
        conversation (list): Conversation history.
    """

    conversation.clear()