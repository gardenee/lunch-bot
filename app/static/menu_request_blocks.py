menu_request_blocks = [
  {
    "type": "header",
    "text": {
        "type": "plain_text",
        "text": "제가 오늘 점심을 추천해드릴게요!",
        "emoji": True
    }
  },
  {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "🏙️ *나의 위치 :*"
    },
    "accessory": {
        "type": "radio_buttons",
        "options": [
            {
                "text": {
                    "type": "plain_text",
                    "text": "발산",
                    "emoji": True
                },
                "value": "발산"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "여의도",
                    "emoji": True
                },
                "value": "여의도"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "상암",
                    "emoji": True
                },
                "value": "상암"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "강남",
                    "emoji": True
                },
                "value": "강남"
            },
            {
                "text": {
                    "type": "plain_text",
                    "text": "서울역",
                    "emoji": True
                },
                "value": "서울역"
            }
        ],
        "initial_option": {
            "text": {
                "type": "plain_text",
                "text": "발산",
                "emoji": True
            },
            "value": "발산"
        }
    }
  },
  {
    "type": "input",
    "element": {
        "type": "plain_text_input",
        "action_id": "not_today_menu_input",
        "placeholder": {
            "type": "plain_text",
            "text": "추천에서 제외할 메뉴들을 적어주세요."
        }
    },
    "label": {
        "type": "plain_text",
        "text": ":nauseated_face: 오늘 먹기 싫은 메뉴 :",
        "emoji": True
    }
  },
  {
    "type": "section",
    "text": {
      "type": "plain_text",
      "text": " "
    }
  },
  {
    "type": "actions",
    "elements": [
        {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "추천받기",
                "emoji": True
            },
            "style": "primary",
            "value": "button_click",
            "action_id": "button_click"
        }
    ]
  }
]
