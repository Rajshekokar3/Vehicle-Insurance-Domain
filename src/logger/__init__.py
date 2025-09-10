import logging 
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from from_root import from_root

#Constants for log configuration
LOG_DIR='logs'
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Max_LOG_SIZE=5* 1024* 1024 #5MB
BACKUP_COUNT=3 #Number os backup log files to keep 


# COnstruct log file path
log_dir_path=os.path.join(from_root(),LOG_DIR) # log directory
os.makedirs(log_dir_path,exist_ok=True) #log file
log_file_Path=os.path.join(log_dir_path,LOG_FILE)

def configure_logger():
    """Congfigures logging with a roating file handlers and console handler"""

    #Create a custom logger 
    logger =logging.getLogger()
    logger.setLevel(logging.DEBUG)

    #Define formatter 
    formatter=logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s-%(message)s")

    #File handler with rotation 
    file_handler=RotatingFileHandler(log_file_Path,maxBytes=Max_LOG_SIZE,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #Console handler 
    console_handler =logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    #Add handlers to the logger 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

#COnfigure the logger 
configure_logger()