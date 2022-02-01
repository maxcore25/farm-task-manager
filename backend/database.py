from model import Todo
import os
from dotenv import load_dotenv

# MongoDB driver
import motor.motor_asyncio

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
