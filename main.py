from fastapi import FastAPI
from backend.user import router

app=FastAPI()

app.include_router(router)


  