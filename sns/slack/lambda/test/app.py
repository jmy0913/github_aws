import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import warnings
warnings.filterwarnings(action='ignore')

def lambda_handler(event:dict, context:str) -> None:
  logging.debug("lambda_handler!!")


  