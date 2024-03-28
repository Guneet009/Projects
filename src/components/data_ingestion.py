import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","data.csv")
    
    """
    import os: This line imports the os module, which provides a way to interact with the operating system in a platform-independent manner.

    train_data_path = os.path.join("artifacts", "train.csv"): This line defines a variable train_data_path and assigns it the result of calling os.path.join() with two arguments: "artifacts" and "train.csv".

    os.path.join() is a function that joins one or more path components intelligently. It constructs a pathname using the appropriate path separator for the operating system. For example, on Unix-like systems (such as Linux or macOS), the separator is "/", while on Windows, it's "".

    In this case, "artifacts" is the first component, representing the directory name, and "train.csv" is the second component, representing the file name. By using os.path.join(), the code ensures that the path is constructed correctly regardless of the operating system being used.
    
    So, the line train_data_path: str = os.path.join("artifacts","train.csv") is simply providing a hint to anyone reading the code (including automated tools) that train_data_path should be a string. It's not strictly necessary for the code to function correctly, but it can help improve readability and maintainability, especially in larger projects where the types of variables might not be immediately obvious from context.
    """
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read data")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            train_set,test_set = (self.ingestion_config.train_data_path,index=False,header=True)
            
            logging.info("Ingestion of data done")
            
            return(
                self.ingestion_config.train_data_path
                self.ingestion_config.test_data_path
            ) 
            
        except Exception as e:
            raise CustomException(e,sys)
        """
        os.path.dirname(self.ingestion_config.train_data_path): This part of the code extracts the directory path from the train_data_path attribute of the ingestion_config object. os.path.dirname() is a function from the os.path module in Python that returns the directory component of a pathname. It takes a file path as input and returns the directory path containing that file. In this case, it extracts the directory portion of the train_data_path. For example, if self.ingestion_config.train_data_path is "artifacts/train.csv", os.path.dirname() will return "artifacts".

        os.makedirs(...): This part of the code is a call to os.makedirs(), which is a function in Python used to create directories recursively. It takes at least one argument, which is the directory path that you want to create. In our case, we're using the directory path extracted from the train_data_path.

        exist_ok=True: This argument tells os.makedirs() to not raise an error if the directory already exists. If exist_ok is set to True, and the directory already exists, os.makedirs() will not raise an error. If exist_ok is False (which is the default), and the directory already exists, os.makedirs() will raise a FileExistsError exception.

        So, putting it all together, this line of code is creating the directory specified by the train_data_path attribute of the ingestion_config object. If the directory already exists, it does nothing (exist_ok=True ensures that). If the directory doesn't exist, it creates it along with any necessary parent directories (os.makedirs() takes care of this with the exist_ok parameter set to True).
                
        """
        # if __name__=="__main__":
        #     obj = DataIngestion()
        #     train_data,test_data = obj.initiate_data_ingestion()
            
        #     data_transformation = DataTransformation()
        #     train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,_test_data)
            
        #     modeltrainer = ModelTrainer()
        #     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
        
        
        
        
        
        
        
        