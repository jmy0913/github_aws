from venv import logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN="xoxb-...."

client = WebClient(token=SLACK_BOT_TOKEN)

# ID of the channel you want to send the message to
channel_id = "......"

try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=channel_id,
        text="Hello"
    )
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")