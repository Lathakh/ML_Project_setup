import logging 
import os
from datetime import datetime


#create logs directory
LOG_DIR =os.path.join(os.getcwd(), 'logs') 
os.makedirs(LOG_DIR,exist_ok=True)

#create log file with timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH=os.path.join(LOG_DIR, LOG_FILE)

# configuring logging
logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

if __name__=="__main__":
    logging.info("logging has successdully setup")
    logging.error("this is the testing error")

   
