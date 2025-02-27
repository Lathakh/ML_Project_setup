import sys
import os
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import  SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


# to create to pkl file to stand, cta-numercial variable
# this function is responsible to all data preprcessing 
    def get_data_transformer_object(self):
        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
                ]

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )  

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),   # missing values  will be handled by this 
                    ("one_hot_encoder",OneHotEncoder()),   # encoding the catergorical into numerical value
                    ("scaler",StandardScaler(with_mean=False))  #  converting within some range
                ]

                
            )

            logging.info("numerical standard scaling completed")

            logging.info("caterogical columns encoding completed")


            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
               
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")

            logging.info("obtaining the preprocessing object")

            preprocessor_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("applyning data preprocessor technique on train ad test dataframe")

            input_features_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_features_test_arr=preprocessor_obj.transform(input_feature_test_df)
            
            # its numpy concatenation function which concatenate the array in column-wise
            train_arr=np.c_[
                input_features_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_features_test_arr,np.array(target_feature_test_df)
            ]
            logging.info("saved the preprocesor object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )  
            logging.info("successfully created pkl file of processor")
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path    # pkl file path of preprocessor
            )
        
            

                  
        except Exception as e:
            raise CustomException(e,sys)
           
            