# ML_Project_setup

# Steps performed
## created new repo in the github
1. clone the repo into local system and opened in VS code
2. install the new environment
3. install requirements.txt - before installing create setup .py file then install
4. created notebook folder
5. save csv file in data folder
6. created EDA notebook file and model file
7. done the all preprocessing in the EDA file 
8. model training in model notebook file .ipynb

# Modular coding

## created project structure src folder
1. created src folder
   1.1 exception  file [exception.py] ----> added custom exception with traceback 
   1.2 logger file [logger.py] ----> logging each step
   1.3 create componets folder 
       #### 1.3.1  data_ingestion.py file  
       1. In this file able ingest data from notebook/data folder first it read data(from cloud also we can do)then perform train test split and save it artifacts folder as train test and raw csv file.Hence it ingestion file return train_data_path and test_data_path. 

       2. Every thing we have performed with single function initiate_data_ingestion inside DataIngestion class.

       3. DataIngestionConfig decorator class to store location of file  

        ##### 1.3.1.1 artifacts  --- train.csv,test.csv,raw.csv   # output of DataIngestsion 
                    
       #### 1.3.2  data_transformation.py file 
       1. In this file we have performed DataTransformation class inside that we have get_data_transformer_object function and initiate_data_transformation .

       2. get_data_transformer_object function:   read the numerical_columns, categorical columns sepeartly and created pipeline perform one hot encoding , stanadard scaler, handle missing value. its return the preprpocessor data.column transformer  module to run bboth num and cat pipeline.

       3. initiate_data_transformation :   In this read the train_data_path and test_data_path from data inegstion as data_train_df dataFrame  -- artifact/ train or test. 

       4. call the  preprocessor_obj to perform preprocessing like one hot encoding,standard scaler  and missing value filling.

       5. defined input feature and target feature by droping from data frame and applied preprocessing obj .

       6. then perform fit_transform  on train data_df and transform  on test data_df and as as arrays.

       7. used np.c_ to concatenate the arrays in column-wise.

       8. call the save object to save the pickel file of  train_data_df and test_data_df  which is define in the util folder.

       9. finally this class return the train_arr, test_arr and pkl file path.  -- that pl file will be cfreated inside artifacts folder artifact/preprocessor.pkl

       10. DataTransformationConfig decorator class to store location of file. 

         ##### 1.3.2.1 artifacts  ---   preprocessor.pkl , train.csv,test.csv,raw.csv    # output of DataTransformation
        

       #### 1.3.3  data_model_trainer.py file  
   1.4     





 
