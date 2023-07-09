import pymongo
import pandas as pd
import json
from dataclasses import dataclass
from pymongo import MongoClient
# Provide the mongodb localhost url to connect python to mongodb.
import os
import certifi

ca = certifi.where()

@dataclass
class EnvironmentVariable:
    mongo_db_url = os.getenv('MONGODB_URL')
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_access_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url, tlsCAFile=ca)
TARGET_COLUMN = "class"