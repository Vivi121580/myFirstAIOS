# myFirstAIOS

A personal AI capability repository for prompts, tools, memory, workflows, local knowledge retrieval, browser-based AI interaction, and user authentication.

## Overview

This project is a local-first personal AI assistant designed to help with:
- reusable prompts
- memory and session tracking
- workflow automation
- local knowledge retrieval
- uploaded file awareness
- browser-based chat UI
- user authentication

## Architecture at a glance

- Frontend: HTML + CSS + JavaScript
- Backend: FastAPI
- Agent layer: custom `PersonalAgent`
- Retrieval: local document indexing and similarity search
- Memory: in-memory and file-backed storage
- Auth: password hashing + SQLite user table
- Persistence: SQLite for user data and chat history

## Quick start

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the environment file:

```bash
cp .env.example .env
```

4. Run the app:

```bash
uvicorn myfirstaios.server:app --reload
```

Then open:

```text
http://localhost:8000/login
```

## Docker

```bash
docker compose up --build
```

## Project structure

```text
myFirstAIOS/
├── Dockerfile
├── README.md
├── ARCHITECTURE.md
├── .dockerignore
├── .env.example
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── src/
│   └── myfirstaios/
│       ├── __init__.py
│       ├── agent.py
│       ├── app.py
│       ├── auth.py
│       ├── chat_store.py
│       ├── config.py
│       ├── knowledge.py
│       ├── memory.py
│       ├── persistent_memory.py
│       ├── prompts.py
│       ├── provider.py
│       ├── rag.py
│       ├── security.py
│       ├── semantic_rag.py
│       ├── server.py
│       ├── session.py
│       ├── tools.py
│       ├── uploads.py
│       ├── user_store.py
│       ├── vector_store.py
│       ├── workflow.py
│       └── web/
│           ├── static/
│           │   ├── app.js
│           │   └── styles.css
│           └── templates/
│               ├── index.html
│               └── login.html
├── tests/
│   ├── test_basic.py
│   └── test_workflow.py
├── data/
└── docs/
```

## Notes

This repo is intentionally built in layers so it can evolve from a simple personal utility into a larger personal AI platform.

It supports:
- local document indexing
- user authentication
- browser chat
- file uploads
- simple memory and workflow primitives
- optional LLM providers

## Next improvements

- Postgres for production data
- JWT auth
- FAISS or pgvector for stronger retrieval
- richer workflow orchestration
- deployment automation
