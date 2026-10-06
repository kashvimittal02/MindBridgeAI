from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# API Key
# ==========================================================

api_key = os.getenv("GEMINI_API_KEY")

# ==========================================================
# Gemini Client
# ==========================================================

client = genai.Client(api_key=api_key)

# ==========================================================
# Model Configuration
# ==========================================================

# Chat Model
MODEL_NAME = "gemini-2.5-flash"

# Embedding Model
EMBEDDING_MODEL = "gemini-embedding-001"

# ==========================================================
# Generation Configuration
# ==========================================================

generation_config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=300
)

# ==========================================================
# RAG Configuration
# ==========================================================

# Maximum characters in one chunk
CHUNK_SIZE = 200

# Characters shared between consecutive chunks
CHUNK_OVERLAP = 50

# Number of chunks retrieved from the vector database
TOP_K = 3