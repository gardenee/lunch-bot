from pydantic import BaseModel
from fastapi import Form

class SlackCommand(BaseModel):
    text: str = ""
    response_url: str
    user_id: str
    user_name: str
    channel_id: str
    team_id: str
    api_app_id: str
    
    @classmethod
    async def as_form(
        cls,
        text: str = Form(default=""),
        response_url: str = Form(...),
        user_id: str = Form(...),
        user_name: str = Form(...),
        channel_id: str = Form(...),
        team_id: str = Form(...),
        api_app_id: str = Form(...)
    ):
        return cls(
            text=text,
            response_url=response_url,
            user_id=user_id,
            user_name=user_name,
            channel_id=channel_id,
            team_id=team_id,
            api_app_id=api_app_id
        )
