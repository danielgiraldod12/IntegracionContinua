import os
from pymongo import MongoClient
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.errors import ConnectionFailure

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get():
    try:
        client = MongoClient('mongodb://localhost:27017/test', serverSelectionTimeoutMS=1000)
        client.server_info()
        return {"connected to bd"}
    except ConnectionFailure as e:
        print("No se puede conectar a MongoDB:", e)
        return {"connected": False, "error": str(e)}
    except Exception as e:
        print("Ocurrió un error:", e)
        return {"connected": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)