from model import Todo
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
db = client.test
