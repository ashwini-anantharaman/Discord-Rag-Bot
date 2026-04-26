import discord
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# RAG setup
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
client = OpenAI()

def ask(question):
    docs = db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant that answers questions based on Paul Graham's essays. Use this context to answer. If you don't know, say so.\n\nContext:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Discord setup
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        question = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if not question:
            await message.reply("Ask me anything about Paul Graham's essays!")
            return
        async with message.channel.typing():
            response = ask(question)
        await message.reply(response)

bot.run(os.getenv("DISCORD_TOKEN"))