from src.pipeline.training_pipeline import start_training_pipeline
from src.pipeline.batch_prediction import start_batch_prediction

file_path=r"G:\100-days-of-dl\Krish_Naik\FSDS_Ineuron_Course\projects\sensor-fault-detection-continuous-training\notebooks\aps_failure_training_set1.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)