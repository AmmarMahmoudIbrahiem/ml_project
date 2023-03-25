import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass 


@dataclass
class DataIngestionConfig:
    train_data_path :str=os.path.join('artifacts','train.csv')
    test_data_path :str=os.path.join('artifacts','test.csv')
    raw_data_path :str=os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self):
         self.ingestion_data=DataIngestionConfig()

    def initiate_data_ingestion(self) :
        logging.info("Enter the data intgestion method")
        try:
            df=df.read_csv('notebook\data\stud.csv')
            os.makedirs(os.path.dirname(self.ingestion_data.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_data.raw_data_path)

            logging.info("traing test split")
            train_set,test_est=train_test_split(df,test_size=0.2)
            train_set.to_csv(self.ingestion_data.train_data_path,index=False,header=True)
            
            test_est.to_csv(self.ingestion_data.test_data_path,index=False,header=True)
            logging("the completed dat ingestion")

            return(
                self.ingestion_data.train_data_path,
                self.ingestion_data.test_data_path,
            )

        except Exception as e:
            raise CustomException(sys,e)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)






