from app.service.llm_agent import run_agent
from app.static.lunch_bot_prompt import get_lunch_bot_prompt

async def recommend_lunch(location: str, not_today_menu: str, channel_id: str):
  ''' LLM을 통해 점심 추천 '''
  
  response = await run_agent(get_lunch_bot_prompt(location, not_today_menu, channel_id))
  print(response)
  
  return response if response else "No response"
