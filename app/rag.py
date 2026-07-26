
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from app.config import CHROMA_PATH, LLM_MODEL
from app.prompt import PROMPT_TEMPLATE
from app.get_embedding_function import get_embedding_function
from pathlib import Path

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=get_embedding_function()
)

model = ChatOllama(
    model=LLM_MODEL
)

def retrieve_documents(query: str, k: int = 3, fetch_k: int = 10):
    results = db.max_marginal_relevance_search(
        query,
        k=k,
        fetch_k=fetch_k
    )
    return results


def build_context(documents):
    return "\n\n----------------------------------------\n\n".join(
        [doc.page_content for doc in documents]
    )


def ask(query: str):
    documents = retrieve_documents(query)

    context = build_context(documents)

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=query
    )

    response = model.invoke(prompt)

    sources = [
        {
         "file": Path(doc.metadata.get("source")).name,
         "page": doc.metadata.get("page"),
        }
        for doc in documents
    ]

    return {
        "answer": response.content,
        "sources": sources,
    }


if __name__ == "__main__":
    query = "What is fraud under Section 17 of the Contract Act?"

    result = ask(query)

    print("\nAnswer:\n")
    print(result["answer"])

    print("\nSources:\n")

    for source in result["sources"]:
        print(f"📄 {source['file']}  |  Page {source['page']}")

