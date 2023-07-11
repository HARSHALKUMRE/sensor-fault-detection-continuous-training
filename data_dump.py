import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://hktech:hktech@cluster0.pvyawg9.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH="G:\\100-days-of-dl\\Krish_Naik\\FSDS_Ineuron_Course\\projects\\sensor-fault-detection-continuous-training\\aps_failure_training_set1.csv"
DATABASE_NAME="Harshal"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)