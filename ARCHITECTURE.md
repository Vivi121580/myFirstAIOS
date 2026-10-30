# Architecture

## 1. Overview

`myFirstAIOS` is a local-first personal AI assistant built to support private, personal workflows and knowledge retrieval. The system is intended to evolve from a simple project prototype into a more capable personal AI platform.

## 2. Goals

- provide a useful personal AI assistant through the browser
- support local file and note retrieval
- remember user context and preferences
- store chat history
- allow uploaded files to be referenced in chat
- keep the architecture modular and easy to extend
- support multiple users with authentication
- allow optional use of cloud or local LLM providers

## 3. Non-goals

This project is not initially intended to be:
- a large multi-tenant SaaS system
- a fully production enterprise security stack
- a distributed high-throughput AI system

## 4. Architecture principles

- modularity
- local-first design
- simplicity
- extensibility
- security by default

## 5. Architecture layers

### 5.1 Frontend

The frontend is a lightweight browser UI built with HTML, CSS, and JavaScript.

Responsibilities:
- render login and chat screens
- send user messages to the backend
- upload files
- display assistant responses

### 5.2 API layer

The API layer is implemented with FastAPI.

Responsibilities:
- serve pages and static assets
- validate requests
- enforce auth
- route requests to the agent
- return responses to the browser

### 5.3 Agent layer

The agent is the central orchestrator.

Responsibilities:
- build prompt payloads
- combine retrieval context
- call the LLM provider
- support tool execution

### 5.4 Retrieval layer

The retrieval layer scans local documents and project files for relevant context.

Responsibilities:
- index text files
- search for relevant snippets
- send context to the agent

### 5.5 Memory layer

Memory stores personal preferences and prior context.

Responsibilities:
- session memory
- short-term context
- persistent memory storage

### 5.6 Auth layer

The auth layer manages user registration and login.

Responsibilities:
- create users
- hash and verify passwords
- protect routes
- maintain session cookies

### 5.7 Storage layer

Current storage is intentionally lightweight and local-first.

Responsibilities:
- persist users
- persist chat history
- store uploaded files

## 6. Major components

### `agent.py`
Central orchestrator of the application.

### `provider.py`
Abstraction over OpenAI and Ollama providers.

### `knowledge.py`
Scans local files and prepares documents for retrieval.

### `vector_store.py`
Builds a lightweight retrieval index using frequency-based embeddings.

### `semantic_rag.py`
Retrieves relevant text from local knowledge and injects it into prompts.

### `memory.py`
Stores in-memory memory objects with topic/content metadata.

### `persistent_memory.py`
Adds file-backed memory persistence.

### `chat_store.py`
Stores per-user chat history in SQLite.

### `user_store.py`
Stores user credentials.

### `server.py`
Main FastAPI app entry point.

### `uploads.py`
Stores uploaded files for later retrieval or analysis.

## 7. Data flow

### Login flow
1. User submits username and password.
2. Backend checks the user store.
3. Password is verified.
4. Backend sets a cookie-based session.
5. Subsequent requests validate the session.

### Chat flow
1. User sends message from UI.
2. API validates auth.
3. Agent builds a prompt with retrieved context.
4. LLM provider generates a response.
5. Response is returned to UI.
6. Chat is saved in chat history.

### Upload flow
1. User uploads a file.
2. Server saves it to the upload directory.
3. File can later be indexed or referenced by the assistant.

## 8. Security

- password hashing
- environment variables for secrets
- route protection
- cookie-based session validation

## 9. Persistence

Current version uses:
- SQLite for user credentials
- SQLite for chat history
- local file system for uploads
- JSON file-backed memory for basic persistence

## 10. Deployment

The app runs locally via uvicorn and can be containerized with Docker.

## 11. Future improvements

- JWT auth
- Postgres
- pgvector or FAISS
- stronger retrieval indexing
- user workspaces
- background jobs

## 12. Summary

`myFirstAIOS` is designed as a modular, local-first personal AI assistant. The architecture is intentionally small but extensible, which makes it useful as a prototype and a solid base for future productization.
