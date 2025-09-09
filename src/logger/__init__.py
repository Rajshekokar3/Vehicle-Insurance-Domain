import logging 
import os
from logging.handlers import RoatatingFileHandler
from datetime import datetime

#Constants for log configuration
LOG_DIR='logs'
LOG_FILE=f"{datetime.now().strftime('%m_%d_')}"