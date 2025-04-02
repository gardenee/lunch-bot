from app.utils.logging import setup_agent_logger, log_agent_action
import json

# ... existing code ...

def run_agent(query: str):
    """
    Agent를 실행하고 결과를 반환합니다.
    """
    logger = setup_agent_logger()
    logger.info(f"사용자 질문: {query}")
    
    try:
        # MCP 클라이언트 초기화
        client = MultiServerMCPClient()
        
        # 날씨 확인
        logger.info("날씨 정보 요청 중...")
        weather_result = client.get_weather()
        logger.info(f"날씨 응답: {json.dumps(weather_result, ensure_ascii=False, indent=2)}")
        
        # 위치 정보 파싱
        location = "강남"  # 예시 - 실제로는 query에서 파싱
        logger.info(f"위치 정보 요청 중... (위치: {location})")
        location_info = client.get_location_info(location)
        logger.info(f"위치 정보 응답: {location_info}")
        
        # 음식점 검색
        rect = location_info  # 위치 정보로부터 얻은 좌표
        logger.info("음식점 검색 중...")
        restaurant_result = client.search_restaurant(menu="라면", rect=rect)
        logger.info(f"음식점 검색 응답: {json.dumps(restaurant_result, ensure_ascii=False, indent=2)}")
        
        # Slack 메시지 생성
        logger.info("Slack 메시지 블록 생성 중...")
        restaurants = [
            {
                "name": "땀땀 본점",
                "main_menu": "라면",
                "address": "서울 강남구 강남대로98길 12-5",
                "map_url": "http://place.map.kakao.com/1238400864"
            }
        ]  # 예시 - 실제로는 restaurant_result에서 파싱
        
        blocks = client.get_response_slack_blocks(restaurants=restaurants)
        logger.info(f"생성된 Slack 블록: {json.dumps(blocks, ensure_ascii=False, indent=2)}")
        
        # Slack으로 메시지 전송
        logger.info("Slack으로 메시지 전송 중...")
        slack_response = client.send_slack_message(
            channel_id="C08L7MHN5J5",
            blocks=blocks
        )
        logger.info(f"Slack 응답: {slack_response}")
        
        return {"status": "success", "message": "Agent execution completed"}
        
    except Exception as e:
        logger.error(f"Agent 실행 중 오류 발생: {str(e)}")
        return {"status": "error", "message": str(e)}

# ... existing code ... 