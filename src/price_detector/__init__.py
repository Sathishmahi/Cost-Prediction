import logging
from price_detector.constant import LOG_FILE_PATH


FORMAT_STR = f"[  %(asctime)s     %(filename)s     %(funcName)s   %(lineno)d ]      [  %(message)s ] "
logging.basicConfig(

    filename = LOG_FILE_PATH,
    format = FORMAT_STR,
    level=logging.INFO,

)