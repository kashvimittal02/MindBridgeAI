from config import client, EMBEDDING_MODEL
"""
embedder.py

Generates vector embeddings for both document chunks
and user queries.
"""

from config import client, EMBEDDING_MODEL


def create_document_embeddings(chunks):
    """
    Generates embeddings for document chunks.

    Args:
        chunks (list[str]): List of document chunks.

    Returns:
        list[list[float]]: List of embedding vectors.
    """

    # Store all embedding vectors
    embeddings = []

    # Gemini allows a maximum of 100 inputs per embedding request.
    # So we split the chunks into batches of 100.
    for i in range(0, len(chunks), 100):

        # Get the next batch of up to 100 chunks
        batch = chunks[i:i + 100]

        # Send only this batch to the embedding model
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=batch
        )

        # Store the embedding vector for every chunk
        for embedding in response.embeddings:
            embeddings.append(embedding.values)

    return embeddings


def create_query_embedding(query):
    """
    Generates an embedding for a user's question.

    Args:
        query (str): User's question.

    Returns:
        list[float]: Embedding vector for the query.
    """

    # Send the user's question to the embedding model
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query
    )

    # Return the embedding vector for the query
    return response.embeddings[0].values