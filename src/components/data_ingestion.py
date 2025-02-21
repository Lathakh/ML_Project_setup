import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:   # data ingestion know that where to save in respective data path
    train_data_path:str=os.path.join("artifacts","train.csv")  # it will the data file in artiface folder
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw_data.csv")

class DataIngestion:
    def __init__(self):  # 3 data path will be save din the  ingestion_config class variable
        self.ingestion_config=DataIngestionConfig()

# to read the data from cloud like mangodb , or you can craete function to read the data  from cloud in utils folder as well
    def initiate_data_ingestion(self):
        logging.info("entered data ingestion method component")

        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("read the dataset as dataframe")

# which create 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True)


            logging.info("train_test _split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            logging.info("ingestion of the data is completed successfully")       

            return (

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            

   
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()      



   

