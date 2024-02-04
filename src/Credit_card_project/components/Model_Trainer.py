import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, mean_absolute_error,accuracy_score
from sklearn.model_selection import GridSearchCV




class ModelTrainer: 
    def __init__(self, config: ModelTrainerConfig): 
        self.config=config
        logger.info(f"final model : {config.final_model}")
        self.Model={
            'Random_Forest': RandomForestClassifier(),
            'Decision_Tree': DecisionTreeClassifier(),
            'NaiveBayes': GaussianNB()
            }  
                
          
    def Model_evaluation(self, Model, x_train, y_train, x_test, y_test): 
        report={}
        mean_error={}
        
        for mod in range(len(Model)): 
            
            model=list(Model.values())[mod]
            model.fit(x_train, y_train)
            
            logger.info(f"Model fitted")
            
            y_pred=model.predict(x_test)
            
            score=accuracy_score(y_test, y_pred)
            mqe=mean_squared_error(y_test, y_pred)
            
            logger.info(f"accuracy score {score} and mean sq error {mqe}")
            
            report[list(Model.keys())[mod]]=score
            mean_error[list(Model.keys())[mod]]=mqe
        
        return report, mean_error
    
    def fine_tune_model(self, best_model: object, x_train, y_train): 
        # 'n_estimators': Number of trees in the forest.
        # max_depth: Definition: Maximum depth of the individual trees.
        # min_samples_split:  Minimum number of samples required to split an internal node.
        # min_samples_leaf: Minimum number of samples required to be at a leaf node.
        # max_features:  The number of features to consider when looking for the best split.
        params={
            'n_estimators': [50, 100],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2],
            'max_features':  ['auto', None]
            
        }
        y_train=np.array(y_train).ravel()
        
        clf=GridSearchCV(best_model, param_grid=params, cv=5, verbose=3)
        clf.fit(x_train, y_train)
        
        best_param=clf.best_params_
        
        logger.info(f"best params :{best_param}")
        
        fine_tune_model=best_model.set_params(**best_param)
        
        return fine_tune_model
        
        
        
             
    def initiate_model_trainer(self): 
        train_path=self.config.train_data_path
        test_path=self.config.test_data_path
        
        ## Loading model path: 
        x=pd.read_csv(train_path)
        y=pd.read_csv(test_path)
        
        # logger.info(f"x_train_ data {x.head()}")
        # logger.info(f"x_test data {y.head()}")   
        
        x_train=x.iloc[:,:-1]
        y_train=x.iloc[:,[-1]]
        x_test=y.iloc[:,:-1]  
        y_test=y.iloc[:,[-1]]
        
        # logger.info(f"x_train_data: \n\n {x_train.shape}")
        # logger.info(f"x_test data:  \n\n {y_train.shape}")
        # logger.info(f"x_test data:  \n\n {x_test.shape}")
        # logger.info(f"x_test data:  \n\n {y_test.shape}")
        
        Model_acc_report, mean_sq_error=self.Model_evaluation(self.Model, x_train, y_train, x_test, y_test)
        
        logger.info(f"Model accuracy report: {Model_acc_report}\n\n")
        logger.info(f"Mean squared error: {mean_sq_error}")
        
        best_model_score=max(sorted(Model_acc_report.values()))
        
        logger.info(f"Best model accuracy {best_model_score}")
        
        best_model_name=list((Model_acc_report.keys()))[list(Model_acc_report.values()).index(best_model_score)]
        
        logger.info(f"Best model Name: {best_model_name}")
        
        best_model_obj=self.Model[best_model_name]
        logger.info(f"best Model {best_model_obj}")
        
        # Fine tuning best model
        Good_model=self.fine_tune_model(best_model_obj, x_train, y_train)
        
        logger.info(f"best model: {Good_model}")
        
        # save_binaryFile(path=Path(self.config.final_model), data=Good_model)
        
        
        y_pre=Good_model.predict(x_test)
        
        score=accuracy_score(y_test, y_pre)
        logger.info(f"After fine tune score {score}")
        
        save_binaryFile(path=Path(self.config.final_model), data=Good_model)
        logger.info(f"Save model sucessful")
        
        
        
        
        