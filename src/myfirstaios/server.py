from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from myfirstaios.agent import PersonalAgent
from myfirstaios.auth import router as auth_router
from myfirstaios.chat_store import ChatStore
from myfirstaios.semantic_rag import SemanticRAG
from myfirstaios.uploads import save_upload

app = FastAPI(title="myFirstAIOS")

project_root = Path(__file__).resolve().parents[2]
rag = SemanticRAG(project_root)
agent = PersonalAgent()
chat_store = ChatStore()

app.include_router(auth_router)
app.mount("/static", StaticFiles(directory=str(Path(__file__).resolve().parent / "web" / "static")), name="static")

templates = Jinja2Templates(directory=str(Path(__file__).resolve().parent / "web" / "templates"))


@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/")
async def index(request: Request):
    username = request.cookies.get("username")
    if not username:
        return RedirectResponse("/login")
    return templates.TemplateResponse("index.html", {"request": request, "username": username})


@app.post("/chat")
async def chat(request: Request, payload: dict) -> dict:
    username = request.cookies.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_input = payload.get("message", "").strip()
    if not user_input:
        return {"reply": "Please provide a message."}

    reply = agent.respond(user_input)
    reply += "\n\nRelevant knowledge:\n" + rag.answer(user_input)
    chat_store.save(username, user_input, reply)
    return {"reply": reply}


@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...)) -> dict:
    username = request.cookies.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")

    content = await file.read()
    saved_path = save_upload(file.filename or "upload.txt", content)
    return {"status": "ok", "path": saved_path}
