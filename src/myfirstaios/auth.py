from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from myfirstaios.security import hash_password, verify_password
from myfirstaios.user_store import UserStore

router = APIRouter()
user_store = UserStore()


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/signup")
async def signup(payload: UserCreate):
    if not payload.username or not payload.password:
        raise HTTPException(status_code=400, detail="Username and password required")

    existing = user_store.get_user(payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user_store.create_user(payload.username, hash_password(payload.password))
    return {"status": "ok"}


@router.post("/login")
async def login(payload: UserLogin):
    user = user_store.get_user(payload.username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"status": "ok", "username": payload.username}
