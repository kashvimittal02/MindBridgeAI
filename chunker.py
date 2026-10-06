"""
chunker.py

Splits extracted text into smaller chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


def create_chunks(text):
    """
    Splits text into overlapping chunks.

    Args:
        text (str): Text extracted from the PDF.

    Returns:
        list[str]: List of text chunks.
    """

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    return chunks