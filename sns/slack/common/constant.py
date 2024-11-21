import enum 

class SLACK_TOKENS(enum.Enum):
  SLACK_BOT_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_BOT_TOKEN")
  SLACK_APP_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_APP_TOKEN")
  SLACK_SIGNING_SECRET = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_SIGNING_SECRET")

class SLACK_CHANNELS(enum.Enum):
  C01V5MJUQ3Y = (enum.auto(), "일반")
  C01V9CP9ZU5 = (enum.auto(), "랜덤")
