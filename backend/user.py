from fastapi import APIRouter
from pymongo import MongoClient

#.env import
import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("MONGO_URI")
print(uri)

mongo = MongoClient(uri)
db = mongo["db"]
users= db["users"]

router = APIRouter()


@router.post("/singup")
def signup(username:str,email:str,password:str):
    dict ={"username":username,
           "email":email,
           "password":password
           }
    users.insert_one(dict)
    return "success"
    pass