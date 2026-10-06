from .embedder import create_query_embedding


def retrieve(query, vector_db, top_k):
    """
    Retrieves the most relevant chunks for a user's question.
    """

    # Convert the user's question into an embedding
    query_embedding = create_query_embedding(query)

    # Search the vector database
    chunks = vector_db.search(
        query_embedding=query_embedding,
        top_k=top_k
    )

    return chunks