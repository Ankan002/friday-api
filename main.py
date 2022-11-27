from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv
from google.cloud import dialogflow_v2 as dialogflow
from pydantic import BaseModel
from config import create_google_credentials_env

app = FastAPI()

if getenv("PY_ENV") != "production":
    load_dotenv()
else:
    create_google_credentials_env.createGoogleCredentialsEnv()


session_client = dialogflow.SessionsClient()


class ChatBody(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Hello from chat-bot api!!"
    }


@app.post("/chat")
async def chat(body: ChatBody):
    try:
        user_msg = body.msg

        session = session_client.session_path(
            getenv("GOOGLE_PROJECT_NAME"), "cherry")

        msg_input = dialogflow.TextInput(
            text=user_msg,
            language_code="en"
        )

        query_input = dialogflow.QueryInput(
            text=msg_input
        )

        response = session_client.detect_intent(
            request={
                "session": session,
                "query_input": query_input
            }
        )

        return {
            "success": True,
            "data": {
                "reply": response.query_result.fulfillment_text
            }
        }

    except Exception:
        print(f"{Exception}")
        return {
            "success": False,
            "error": "Some Error Occurred!! Please contact the owner..."
        }
