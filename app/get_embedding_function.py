from langchain_ollama import OllamaEmbeddings

from app.config import EMBEDDING_MODEL


def get_embedding_function():
    embedding = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )
    return embedding