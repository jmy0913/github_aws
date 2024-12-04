import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import warnings
warnings.filterwarnings(action='ignore')

from sns_slack import slack_alarm
from constant import SLACK_CHANNELS, SERVICE_TYPE

def lambda_handler(event:dict, context:str) -> None:
  logging.info("lambda_handler!!")
  logging.info(f"event: {str(event)}")


  