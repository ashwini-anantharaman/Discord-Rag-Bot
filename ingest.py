from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

print("Loading essays...")
docs = []
for file in os.listdir("docs"):
    if file.endswith(".txt"):
        try:
            loader = TextLoader(f"docs/{file}", encoding="utf-8")
            docs.extend(loader.load())
        except:
            print(f"Skipped {file}")

print(f"Loaded {len(docs)} essays")

print("Chunking...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

print("Embedding and storing in ChromaDB...")
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")
print(f"Done! {len(chunks)} chunks stored in ChromaDB")