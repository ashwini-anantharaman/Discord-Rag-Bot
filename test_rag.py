from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
client = OpenAI()

def ask(question):
    # Retrieve relevant chunks
    docs = db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Generate answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. Use this context from Paul Graham's essays to answer the question. If you don't know, say so.\n\nContext:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

question = "What does Paul Graham say about how to get startup ideas?"
print(f"Q: {question}")
print(f"A: {ask(question)}")