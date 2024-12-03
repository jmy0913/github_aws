import enum 

class SLACK_TOKENS(enum.Enum):
  SLACK_BOT_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_BOT_TOKEN")
  SLACK_APP_TOKEN = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_APP_TOKEN")
  SLACK_SIGNING_SECRET = (enum.auto(), "/sns/slack/aws-slack-tutorial/SLACK_SIGNING_SECRET")

class SLACK_CHANNELS(enum.Enum):
  ALARM = (enum.auto(), "C083BP1SXPV", "알람")
  ERROR = (enum.auto(), "C0840KN4H9N", "에러")
