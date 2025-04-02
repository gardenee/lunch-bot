import os
from dotenv import load_dotenv
import httpx
import certifi

load_dotenv()
    

def post_slack_message(channel_id: str, blocks: list = None, text: str = None, thread_ts: str = None):
    """
    Slack sdk와 연동해서 메시지를 전송
    """
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {os.getenv('SLACK_BOT_TOKEN')}",
        "Content-Type": "application/json"
    }
    data = {
        "channel": channel_id,
        "text": " ",
        **{key: value for key, value in {
            "blocks": blocks,
            "text": text,
            "thread_ts": thread_ts
        }.items() if value}
    }
    with httpx.Client(verify=certifi.where()) as client:
        res = client.post(url, json=data, headers=headers)
        print(res.status_code)
        print(res.text)


def parse_slack_response(payload: dict) -> dict:
    """
    Slack response에서 action type을 기준으로 값을 파싱하는 함수
    """
    location, not_today_menu_value = None, None
    values = payload.get("state", {}).get("values", {})
    
    for _, actions in values.items():
        for _, action in actions.items():
            action_type = action.get("type")
            if action_type == "radio_buttons":
                selected_option = action.get("selected_option", {})
                text_value = selected_option.get("text", {}).get("text", "")
                location = text_value
            elif action_type == "plain_text_input":
                not_today_menu_value = action.get("value", "")
            
    return location, not_today_menu_value
  