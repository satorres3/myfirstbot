# Agents

This project envisions AI assistants that can be configured per department. Agents are thin wrappers around external large language models accessed via providers such as OpenAI, Google Gemini, or other APIs. Future work may integrate frameworks like LangChain to orchestrate retrieval augmented generation and custom knowledge bases.

## Architecture

```
user query -> embedding -> vector search -> LLM -> response
```

`hub.views` contains placeholder endpoints where agent calls can be inserted. Configuration (API keys, model selection) will live in database settings and be exposed through a UI page.

## Customization

- Add new providers by implementing a class in `agents/` that follows a simple `generate(prompt)` interface.
- Register the class via Django settings or an admin panel.
- Swap models at runtime by selecting the desired provider in the settings page.

## Knowledge Base Setup

Knowledge bases will be stored using vector databases such as FAISS or external services like Pinecone. Documents can be uploaded per department; embeddings are computed via `SentenceTransformers` and persisted for retrieval.
