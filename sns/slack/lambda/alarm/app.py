import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import warnings
warnings.filterwarnings(action='ignore')

from common.sns_slack import slack_alarm
from common.constant import SLACK_CHANNELS, SERVICE_TYPE

def lambda_handler(event:dict, context:str) -> None:
  logging.info("lambda_handler!!")
  logging.info(f"event: {str(event)}")

  slack = slack_alarm(p_slack_channel=SLACK_CHANNELS.ERROR)
  logging.info("create a slack")
  
  return event 
