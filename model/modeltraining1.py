#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("I am the BEST")


# In[3]:


from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents():
    document_loader = PyPDFDirectoryLoader(r"C:\Users\akhil\My_projects\ai_lawyer\data\books")
    return document_loader.load()


# In[4]:


documents = load_documents()
print(documents[0].page_content[:50])


# In[5]:


print("I am the Fucking No. 1")


# In[6]:


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)



# In[7]:


documents = load_documents()
chunks = split_documents(documents)
print(chunks[0])


# In[8]:


print(chunks[50])


# In[9]:


from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings


# In[10]:


import sys
print(sys.executable)


# In[11]:


import sys
get_ipython().system('{sys.executable} -m pip show langchain-ollama')


# In[12]:


from get_embedding_function import get_embedding_function

embeddings = get_embedding_function()
print(len(embeddings.embed_query("hello")))


# In[13]:


from langchain_chroma import Chroma
print("OK")


# In[14]:


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


# In[15]:


for chunk in chunks[:5]:
    print(chunk.metadata["id"])


# In[16]:


from langchain_chroma import Chroma
from langchain_core.documents import Document
from get_embedding_function import get_embedding_function

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embedding_function()
    )
    db.add_documents(chunks)


# In[17]:


from langchain_core.documents import Document

docs = [
    Document(page_content="Section 420 IPC deals with cheating")
]

add_to_chroma(docs)
print("Stored successfully")


# In[18]:


from langchain_chroma import Chroma
from get_embedding_function import get_embedding_function

CHROMA_PATH = "./chroma_db"

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=get_embedding_function()
)


# In[19]:


print(type(db))


# In[20]:


existing_items = db.get(include=[])

existing_ids = set(existing_items["ids"])

print(f"Existing documents: {len(existing_ids)}")


# In[21]:


new_chunks = []

for chunk in chunks:
    if chunk.metadata["id"] not in existing_ids:
        new_chunks.append(chunk)

print(f"New chunks: {len(new_chunks)}")


# In[23]:


test_chunks = new_chunks[:5]

db.add_documents(
    test_chunks,
    ids=[chunk.metadata["id"] for chunk in test_chunks]
)


# In[24]:


print(len(documents))
print(len(chunks))


# In[25]:


BATCH_SIZE = 40

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


# In[26]:


query = "What is Article 21?"

results = db.similarity_search(query, k=3)

results


# In[27]:


for result in results:
    print(result.page_content)
    print("-" * 100)


# In[30]:


from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from get_embedding_function import get_embedding_function


# In[31]:


CHROMA_PATH = "chroma_db"

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=get_embedding_function()
)


# In[32]:


query_text = "What is Article 21?"


# In[33]:


results = db.similarity_search_with_score(query_text, k=5)

results


# In[34]:


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context:

{question}
"""


# In[35]:


context_text = "\n\n---\n\n".join(
    [doc.page_content for doc, _score in results]
)


# In[36]:


prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

prompt = prompt_template.format(
    context=context_text,
    question=query_text
)

print(prompt)


# In[37]:


model = OllamaLLM(model="llama3.2")


# In[38]:


response_text = model.invoke(prompt)

print(response_text)


# In[39]:


sources = [
    doc.metadata.get("id", None)
    for doc, _score in results
]

print("Sources:")

for source in sources:
    print(source)


# In[40]:


query = "What are Fundamental Rights?"

results = db.similarity_search(query, k=3)

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print(doc.page_content[:500])
    print("-" * 80)


# In[41]:


from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM


# In[42]:


PROMPT_TEMPLATE = """
You are an AI Legal Assistant.

Answer the user's question ONLY using the context below.

If the answer cannot be found in the context, reply:

"I couldn't find the answer in the provided legal documents."

Context:
{context}

--------------------------------

Question:
{question}

--------------------------------

Answer:
"""


# In[43]:


query = "What is Article 21?"


# In[44]:


results = db.max_marginal_relevance_search(
    query,
    k=3,
    fetch_k=10
)


# In[52]:


context = "\n\n----------------------------\n\n".join(
    [doc.page_content for doc in results]
)


# In[53]:


prompt_template = ChatPromptTemplate.from_template(
    PROMPT_TEMPLATE
)

prompt = prompt_template.format(
    context=context,
    question=query
)

print(prompt[:1500])


# In[54]:


model = OllamaLLM(
    model="llama3.2"
)


# In[55]:


response = model.invoke(prompt)

print(response)

