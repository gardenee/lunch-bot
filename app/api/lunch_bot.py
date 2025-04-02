import json
import asyncio
from fastapi import Depends, APIRouter, Form
from fastapi.responses import Response
from app.model.slack import SlackCommand
from app.static.menu_request_blocks import menu_request_blocks
from app.service.slack import post_slack_message, parse_slack_response
from app.service.lunch_bot import recommend_lunch

router = APIRouter()


@router.post("")
def lunch_bot_response(
    command: SlackCommand = Depends(SlackCommand.as_form)
):
    post_slack_message(
        channel_id=command.channel_id,
        text=command.text,
        blocks=menu_request_blocks
    )
    return Response(status_code=200)    
  
  
@router.post("/actions")
async def handle_slack_actions(payload: str = Form(...)): 
    payload_json = json.loads(payload)
    
    if payload_json["type"] == "block_actions":
        action = payload_json["actions"][0]
        if action["action_id"] == "button_click":
            channel_id = payload_json["channel"]["id"]
            user_id = payload_json["user"]["id"]
            post_slack_message(channel_id, None, f"<@{user_id}>님이 추천받기 버튼을 눌렀어요!")
            
            location, not_today_menu_value = parse_slack_response(payload_json)
            asyncio.create_task(recommend_lunch(location, not_today_menu_value, channel_id))
            
            return Response(status_code=200)
        