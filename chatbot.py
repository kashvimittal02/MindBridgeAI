"""
chatbot.py

Main chatbot class for MindBridge.
Coordinates memory, retrieval and Gemini.
"""

from config import (
    client,
    MODEL_NAME,
    generation_config,
    TOP_K
)

from prompts import SYSTEM_PROMPT

from memory import (
    add_user_message,
    add_assistant_message,
    get_history
)

from RAG.vectordb import VectorDB
from RAG.retriever import retrieve
from RAG.prompt_builder import build_prompt


class MindBridge:
    """
    Main chatbot class.
    """

    def __init__(self):
        """
        Initializes the chatbot.
        """

        # Stores the complete conversation history
        self.conversation = []

        # Create or load the vector database
        self.vector_db = VectorDB()

        # Store the system prompt
        self.system_prompt = SYSTEM_PROMPT
    def needs_retrieval(self, user_query):
        """
        Determines whether the user's question
        should use the document knowledge base.

        Args:
            user_query (str)

        Returns:
            bool
        """

        # Convert to lowercase for easier matching
        query = user_query.lower()

        # Keywords related to the mental health document
        keywords = [
            "mental",
            "stress",
            "anxiety",
            "depression",
            "well-being",
            "wellbeing",
            "healthy",
            "symptoms",
            "therapy",
            "emotion",
            "emotional",
            "psychological"
        ]

        # If any keyword appears,
        # use the RAG pipeline.
        for keyword in keywords:

            if keyword in query:
                return True

        return False

    def retrieve_context(self, user_query):
        """
        Retrieves the most relevant document chunks
        for the user's question.

        Args:
            user_query (str): User's question.

        Returns:
            list[str]: Most relevant document chunks.
        """

        # Retrieve the most relevant chunks
        retrieved_chunks = retrieve(
            query=user_query,
            vector_db=self.vector_db,
            top_k=TOP_K
        )

        return retrieved_chunks

    def build_chat_prompt(self, user_query, retrieved_chunks):
        """
        Builds the final prompt for Gemini.

        Args:
            user_query (str): User's question.
            retrieved_chunks (list[str]): Retrieved RAG context.

        Returns:
            str: Final prompt.
        """

        # Convert the conversation history into a single string
        conversation_history = get_history(
            self.conversation
        )

        # Build the final prompt
        prompt = build_prompt(
            system_prompt=self.system_prompt,
            conversation_history=conversation_history,
            retrieved_chunks=retrieved_chunks,
            user_query=user_query
        )

        return prompt
    def generate_response(self, prompt):
        """
        Sends the prompt to Gemini and returns the response.

        Args:
            prompt (str): Final prompt.

        Returns:
            str: Assistant's response.
        """

        # Send the prompt to Gemini
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=generation_config
        )

        # Return only the generated text
        return response.text
    def update_memory(self, user_query, assistant_response):
        """
        Stores the latest conversation in memory.

        Args:
            user_query (str): User's question.
            assistant_response (str): Assistant's response.
        """

        # Save the user's message
        add_user_message(
            self.conversation,
            user_query
        )

        # Save the assistant's response
        add_assistant_message(
            self.conversation,
            assistant_response
        )
    def chat(self, user_query):
        """
        Processes the user's question and returns
        the assistant's response.

        Args:
            user_query (str): User's question.

        Returns:
            str: Assistant's response.
        """

        # Decide whether retrieval is needed
        if self.needs_retrieval(user_query):

            retrieved_chunks = self.retrieve_context(
                user_query
            )

        else:

            retrieved_chunks = []

        # Build the final prompt
        prompt = self.build_chat_prompt(
            user_query,
            retrieved_chunks
        )

        # Generate Gemini's response
        try:
            assistant_response = self.generate_response(
                prompt
    )

        except Exception as e:
            return f"An error occurred: {e}"
        

        # Store the conversation
        self.update_memory(
            user_query,
            assistant_response
        )

        # Return the response
        return assistant_response