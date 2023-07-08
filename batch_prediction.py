from src.pipeline.training_pipeline import start_training_pipeline
from src.pipeline.batch_prediction import start_batch_prediction
import os

file_path=os.path.join('aps_failure_training_set1.csv')
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)