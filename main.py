from fastapi import FastAPI
from backend.api import router as api_router
from backend.chat_routes import router as chat_router
from frontend.routes import router as frontend_router
from db.session import create_db

app = FastAPI(title="Website API")

app.include_router(api_router)
app.include_router(chat_router)
app.include_router(frontend_router)


@app.on_event("startup")
async def startup_event():
    create_db()
