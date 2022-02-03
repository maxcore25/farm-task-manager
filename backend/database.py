from model import Todo
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGODB_URL"))
db = client.TodoList
collection = db.todo


def fetch_one_todo(title):
    document = collection.find_one({'title': title})
    return document


def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    for document in cursor:
        todos.append(Todo(**document))
    return todos


def create_todo(todo):
    document = todo
    collection.insert_one(document)
    return document


def update_todo(title, desc):
    collection.update_one({'title': title}, {'$set': {'description': desc}})
    document = collection.find_one({'title': title})
    return document


def remove_todo(title):
    collection.delete_one({'title': title})
    return True
