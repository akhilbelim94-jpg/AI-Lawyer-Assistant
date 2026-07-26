from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.config import (
    DATA_PATH,
    CHROMA_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    BATCH_SIZE,
)
from app.get_embedding_function import get_embedding_function

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)

    return document_loader.load()


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)


def main():
    documents = load_documents()
    chunks = split_documents(documents)

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        # Get source and page number
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")

        # Create page identifier
        current_page_id = f"{source}:{page}"

        # Check if we're still on the same page
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Create unique chunk ID
        chunk_id = f"{current_page_id}:{current_chunk_index}"

        # Store ID in metadata
        chunk.metadata["id"] = chunk_id

        # Update last page ID
        last_page_id = current_page_id


    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )


    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Existing documents: {len(existing_ids)}")


    new_chunks = []

    for chunk in chunks:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    print(f"New chunks: {len(new_chunks)}")


    if len(new_chunks) == 0:
        print("No new documents to add.") 

    else:
        total = len(new_chunks)

        for i in range(0, total, BATCH_SIZE):
            batch = new_chunks[i:i + BATCH_SIZE]

            db.add_documents(
                batch,
                ids=[chunk.metadata["id"] for chunk in batch]
            )

            print(f"Added {min(i + BATCH_SIZE, total)} / {total}")

        print("All documents added successfully!")

if __name__ == "__main__":
    main()
