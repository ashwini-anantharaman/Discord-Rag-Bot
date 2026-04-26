# Discord-Rag-Bot
Discord RAG bot which gives Y Combinator Startup Advice using Paul Graham's essays
# Paul Graham Essay Bot 🤖

A Discord RAG bot that answers questions using Paul Graham's essays as a knowledge base.

## How it works
1. Scraped 50+ essays from paulgraham.com
2. Chunked and embedded them using OpenAI embeddings
3. Stored vectors in ChromaDB
4. Discord bot retrieves relevant chunks and generates answers with GPT-4o-mini

## Stack
- Python, Discord.py
- LangChain, ChromaDB
- OpenAI API

## Setup
1. Clone the repo
2. Create a `.env` file with `DISCORD_TOKEN` and `OPENAI_API_KEY`
3. Run `pip install -r requirements.txt`
4. Run `python ingest.py` to build the knowledge base
5. Run `python bot.py` to start the bot
