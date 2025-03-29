import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrockConverse
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

def get_model():
    return ChatBedrockConverse(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        aws_region=os.getenv("AWS_REGION")
    )


def get_mcp_server_params():
    return MultiServerMCPClient(
        {
            "slack": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-slack"],
                "env": {
                    "SLACK_BOT_TOKEN": os.getenv("SLACK_BOT_TOKEN", ""),
                    "SLACK_TEAM_ID": os.getenv("SLACK_TEAM_ID", "")
                }
            }
        }
    )


def get_mcp_servers():
    return {
        "mcpServers": {
            "slack": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-slack"],
                "env": {
                    "SLACK_BOT_TOKEN": os.getenv("SLACK_BOT_TOKEN", ""),
                    "SLACK_TEAM_ID": os.getenv("SLACK_TEAM_ID", "")
                }
            }
        }
    }

mcp_servers = get_mcp_servers() 