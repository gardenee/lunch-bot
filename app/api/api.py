from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health")
async def health_check():
    return {"status": "healthy"} 

@api_router.post("lunch-bot-response")
async def lunch_bot_response():
    
    
    return {}