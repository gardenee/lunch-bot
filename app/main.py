from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(title="LunchBot Client")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8888, reload=True) 
    