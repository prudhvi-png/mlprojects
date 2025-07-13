import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd   
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')   ## Defining parths for the data sets 
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\Data\Student.csv")  # Reading the dataset from some where
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path,),exist_ok=True) ##

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) ## Converted into data frame

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42) ## Doing train test split

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) ## Saving into the folder of train data

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True) ## Saving the test data info file

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
    

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
