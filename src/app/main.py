import os
import asyncio

from fastapi import FastAPI, Response, status
from dotenv import load_dotenv
from agents.root_agent import trigger_agent
from schemas.webhook_request import WebhookRequest

load_dotenv()

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to project_healer."}


@app.get("/healthcheck")
async def healthcheck():
    # response = await trigger_agent(
    #     "list all the latest commits of the repository google_adk_demo_1. with atulGupta2922 as owner of the repository."
    # )
    return {"success": True, "healthcheck": "healthy"}


@app.post("/receive-alert")
async def receive_alert(request: WebhookRequest, response: Response):
    try:
        result = await trigger_agent(request.alert_payload)
        response.status_code = status.HTTP_200_OK
        return {"success": True, "message": result}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        raise e
