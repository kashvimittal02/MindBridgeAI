"""
vectordb.py

Stores and retrieves document embeddings using ChromaDB.
"""

import chromadb


class VectorDB:
    """
    Handles all interactions with the vector database.
    """

    def __init__(self):

        # Create a persistent ChromaDB client.
        # Saves everything to disk so the database is not lost
        # when we restart the application.
        self.client = chromadb.PersistentClient(path="./vector_db")

        # Create the collection if it doesn't exist,
        # otherwise load the existing one.
        # A collection is similar to a SQL table.
        # It stores IDs, text chunks and their embeddings.
        self.collection = self.client.get_or_create_collection(
            name="mindbridge"
        )

    def add_documents(self, document_name, chunks, embeddings):
        """
        Store chunks and their embeddings.
        """

        # Every chunk must have exactly one embedding.
        # Otherwise the database won't know which embedding
        # belongs to which chunk.
        if len(chunks) != len(embeddings):
            raise ValueError(
                "The number of chunks and embeddings must be equal."
            )

        ids = []

        # Create a unique and readable ID for every chunk.
        # Example:
        # mental_health_chunk_0
        # mental_health_chunk_1
        for i in range(len(chunks)):
            ids.append(f"{document_name}_chunk_{i}")

        # Store the IDs, text chunks and embeddings together.
        # ChromaDB uses embeddings for similarity search,
        # while the text chunks are returned to the LLM.
        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(self, query_embedding, top_k):
        """
        Search the vector database for the most similar chunks.

        Args:
            query_embedding (list[float]): Embedding of the user's question.
            top_k (int): Number of similar chunks to retrieve.

        Returns:
            list[str]: Most relevant text chunks.
        """

        # Search the collection using the query embedding.
        # query_embeddings expects a list because ChromaDB can
        # search for multiple queries at once.
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        # Return only the retrieved text chunks.
        # documents is a nested list:
        # [
        #     [chunk1, chunk2, chunk3]
        # ]
        # Since we searched for only one query,
        # we return the first list.
        return results["documents"][0]