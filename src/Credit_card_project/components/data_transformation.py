import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from src.Credit_card_project.entity.config_entity import DataTransformationConfig
from src.Credit_card_project import logger
from src.Credit_card_project.utils.common import save_object
from pathlib import Path



class DataTransformation: 
    def __init__(self, config: DataTransformationConfig): 
        self.config=config
        logger.info(f"test percentage {config.test_percentage}")
        
    def train_test_data_split(self, data: pd.DataFrame):
        
        # data=pd.read_csv(data)
        train_data, test_data=train_test_split(data, 
                                               test_size=self.config.test_percentage,
                                               random_state=42)
        logger.info(f"train test data split")
        train_data.to_csv(self.config.train_data_path, index=False, header=True)
        logger.info(f"Train data saved : {train_data.shape}")
        test_data.to_csv(self.config.test_data_path, index=False, header=True)
        logger.info(f"test data saved {test_data.shape}")
        
        
    def get_data_preprocessor(self, num_col): 
        
        num_pipeline=Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())])
        preprocess=ColumnTransformer([('num_pipeline', num_pipeline, num_col)])
        return preprocess
        
        
    def data_transformation_initiate(self): 
        
        data_df=pd.read_csv(self.config.data_dir)
        drop_column=['SEX','EDUCATION','MARRIAGE','AGE']
        data=data_df.drop(drop_column, axis=1)
        
        # Train test split
        self.train_test_data_split(data)
        
     
        
        ## Spliting dependent and independent variable.
        train_data_path=self.config.train_data_path
        test_data_path=self.config.test_data_path
       
        
        train_df=pd.read_csv(train_data_path)
        test_df=pd.read_csv(test_data_path)
        logger.info(f"train and test data loaded from data transformation file.")
        
        target_column=self.config.target_column.keys()
        logger.info(f"Target columns: {target_column}")
        
        input_feature_train_df=train_df.drop(target_column, axis=1)
        target_feature_train_df=train_df[target_column]
        
        logger.info(f"Independent Variable Input:  {input_feature_train_df.shape} OUTput {target_feature_train_df.shape}")
        
        input_feature_test_df=test_df.drop(target_column, axis=1 )
        target_feature_test_df=test_df[target_column]
        
        logger.info(f"dependent Variable Input:  {input_feature_test_df.shape} OUTput {target_feature_test_df.shape}")
        
        ## Pipeline for dataTransformation
        
        num_col=[col for col in input_feature_train_df.columns if input_feature_train_df[col].dtypes!='O']
        
        logger.info(f"NUmerical col: {num_col}")
        
        preprocessor=self.get_data_preprocessor(num_col)
        
        logger.info(f"Preprocessor part {preprocessor}")
        
        save_object(file_path=Path(self.config.preprocess_path), obj=preprocessor)
        
        x_train_scaled=preprocessor.fit_transform(input_feature_train_df)
        x_train_scaled_df=pd.DataFrame(x_train_scaled, columns=preprocessor.get_feature_names_out())
        
        
        logger.info(f"x_train sclead data frame{ x_train_scaled_df.head()}")
        
        x_test_scaled=preprocessor.transform(input_feature_test_df)
        x_test_scaled_df=pd.DataFrame(x_test_scaled, columns=preprocessor.get_feature_names_out())

        logger.info(f"x_train sclead { x_test_scaled_df.head()}")
        
        
        target_train=pd.DataFrame(target_feature_train_df, columns=self.config.target_column)
        target_test=pd.DataFrame(target_feature_test_df, columns=self.config.target_column)
        
        train_scaled=pd.concat([x_train_scaled_df, target_train], axis=1)
        test_scaled=pd.concat([x_test_scaled_df, target_test], axis=1)
        
        train_scaled.to_csv(self.config.train_scaled, index=False, header=True)
        test_scaled.to_csv(self.config.test_scaled, index=False, header=True)
        
        logger.info(f"Sucessfully done")
        
        
    

        