import enum 

class SLACK_TOKENS(enum.Enum):
  SLACK_BOT_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_BOT_TOKEN")
  SLACK_APP_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_APP_TOKEN")
  SLACK_SIGNING_SECRET = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_SIGNING_SECRET")

class SLACK_CHANNELS(enum.Enum):
  ALARM = (enum.auto(), "C083BP1SXPV", "알람")
  ERROR = (enum.auto(), "C0840KN4H9N", "에러")

class SERVICE_TYPE(enum.Enum):
  TEST = (enum.auto(), "테스트용입니다.")
  DEV = (enum.auto(), "개발용입니다.")

# https://api.slack.com/reference/block-kit/blocks#actions_examples
class MESSAGE_BLOCKS(enum.Enum):
  SERVICE = (enum.auto(), [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "{service_nm}"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "{service_msg}"
      }
    }
  ], "서비스 메세지")
  ERROR = (enum.auto(), [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "{error_msg}"
      }
    }
  ], "오류 메세지")


