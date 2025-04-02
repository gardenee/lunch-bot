import sys
import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP 

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.model.lunch import RecommendedLunch
from app.static.menu_response_blocks import menu_response_block_header, number_emoji
from app.service.slack import post_slack_message

load_dotenv()
mcp = FastMCP("SlackLunchBot")


@mcp.tool()
def get_weather():
    """Get weather for seoul"""
    params = {
        "q": "seoul",
        "appid": os.getenv('OPENWEATHER_API_KEY'),
        "lang": "kr",
        "units": "metric"
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    with httpx.Client() as client:
        response = client.get(url, params=params)

        return response.json()
  
  
@mcp.tool()
def get_location_info(user_location: str) -> str:
    """
    Get latitude, longitude info from user location
    kakao api의 rect 파라미터로 사용
    rect: 좌측 X 좌표, 좌측 Y 좌표, 우측 X 좌표, 우측 Y 좌표 형식
    """
    if user_location == "발산":
        return "126.826874,37.558873,126.837805,37.562909"
    elif user_location == "여의도":
        return "126.923458,37.521202,126.929495,37.527260"
    elif user_location == "상암":
        return "126.891334,37.573435,126.900282,37.579493"
    elif user_location == "강남":
        return "127.024170,37.497179,127.030297,37.504495"
    elif user_location == "서울역":
        return "126.971300,37.553166,126.976512,37.559510"
    else:
        # default 발산 일대
        return "126.827560,37.564710,126.838274,37.570220"


@mcp.tool()
async def search_restaurant(menu: str, rect: str):
    """
    Search restaurant from kakao search api
    rect: 좌측 X 좌표, 좌측 Y 좌표, 우측 X 좌표, 우측 Y 좌표 형식
    menu: 검색어(ex. 닭갈비, 피자)
    """
    headers = {
        "Authorization": f"KakaoAK {os.getenv('KAKAO_ACCESS_TOKEN')}",
    }
    params = {
        "category_group_code": "FD6",
        "rect": rect,
        "query": menu,
        "size": 15
    }
    url = "https://dapi.kakao.com/v2/local/search/category"
    
    with httpx.Client() as client:
        response = client.get(url, headers=headers, params=params)
        
        return response.json()


@mcp.tool()
def get_response_slack_blocks(restaurants: list[RecommendedLunch]) -> list[dict]:
    """
    Slack blocks 형식으로 추천받은 음식점 변환
    응답은 json 형식이 아니라 반드시 python 객체여야 함.
    """
    blocks = [menu_response_block_header]
    
    for i, restaurant in enumerate(restaurants):
        restaurant_blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{number_emoji[i]}  *{restaurant.name}*"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": f"💃 {restaurant.address}",
                        "emoji": True
                    }
                ]
            },    
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"<{restaurant.map_url}>"
                    }
                ]
            },
        ]
        blocks = blocks + restaurant_blocks
    
    return blocks


@mcp.tool()
def send_slack_message(channel_id: str, blocks: list[dict]):
    """
    Slack blocks 형식으로 추천받은 음식점 정보를 사용자에게 전달
    """
    post_slack_message(channel_id, blocks)
    return 'done'
                
                
if __name__ == "__main__":
    mcp.run(transport="stdio")
