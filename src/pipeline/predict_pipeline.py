# import sys
# import os
# import pandas as pd
# from src.exception import CustomException
# from src.utils import load_object


# class PredictPipeline:
#     def __init__(self):
#         pass

#     def predict(self,features):
#         try:
#             model_path=os.path.join("artifacts","model.pkl")
#             preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
#             print("Before Loading")
#             model=load_object(file_path=model_path)
#             preprocessor=load_object(file_path=preprocessor_path)
#             print("After Loading")
#             data_scaled=preprocessor.transform(features)
#             preds=model.predict(data_scaled)
#             return preds
        
#         except Exception as e:
#             raise CustomException(e,sys)


# class CustomData:
#     def __init__(  self,
#         min_age:int,
#         max_age:int,
#         gender: str,
#         interest:int,
#         impressions:int,
#         clicks:int,
#         spent:float):

#         self.min_age = min_age

#         self.max_age = max_age

#         self.gender = gender

#         self.interest = interest

#         self.impressions = impressions

#         self.clicks = clicks

#         self.spent = spent

#     def get_data_as_data_frame(self):
#         try:
#             custom_data_input_dict = {
#                 "min_age": [self.min_age],
#                 "max_age": [self.max_age],
#                 "gender": [self.gender],
#                 "interest": [self.interest],
#                 "impressions": [self.impressions],
#                 "clicks": [self.clicks],
#                 "spent": [self.spent],
#             }

#             return pd.DataFrame(custom_data_input_dict)

#         except Exception as e:
#             raise CustomException(e, sys)
import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            print("Loading model and preprocessor...")
            self.model = load_object(file_path=model_path)
            self.preprocessor = load_object(file_path=preprocessor_path)
            print("Model and preprocessor loaded successfully!")
        except Exception as e:
            raise CustomException(f"Error loading model/preprocessor: {e}", sys)

    def predict(self, features):
        try:
            expected_columns = ['min_age', 'max_age', 'gender', 'interest', 'Impressions', 'Clicks', 'Spent']
            if not all(column in features.columns for column in expected_columns):
                raise ValueError(f"Missing columns: {set(expected_columns) - set(features.columns)}")
            
            data_scaled = self.preprocessor.transform(features)
            preds = self.model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, min_age: int, max_age: int, gender: str, interest: int, Impressions: int, Clicks: int, Spent: float):
        self.min_age = min_age
        self.max_age = max_age
        self.gender = gender
        self.interest = interest
        self.Impressions = Impressions
        self.Clicks = Clicks
        self.Spent = Spent

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "min_age": [self.min_age],
                "max_age": [self.max_age],
                "gender": [self.gender],
                "interest": [self.interest],
                "Impressions": [self.Impressions],
                "Clicks": [self.Clicks],
                "Spent": [self.Spent],
            }
            input_df = pd.DataFrame(custom_data_input_dict)
            print("Generated input DataFrame:")
            print(input_df.head())
            return input_df
        except Exception as e:
            raise CustomException(f"Error creating DataFrame: {e}", sys)