from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
import uvicorn

if getenv("PY_ENV") != "production":
    load_dotenv()
    
app = FastAPI()

@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Hello from chat-bot api!!"
    }
  
  
if __name__ == "__main__":
    uvicorn.run(app, port=int(getenv("PORT")))