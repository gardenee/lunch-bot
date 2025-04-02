from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.api import lunch_bot

app = FastAPI(title="LunchBot Client")

api_router = APIRouter()
api_router.include_router(lunch_bot.router, prefix="/lunch-bot", tags=["lunch-bot"])

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8888, reload=True) 
    