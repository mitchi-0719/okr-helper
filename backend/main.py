import gemini
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=[
    #     "http://localhost:5173",
    #     "http://127.0.0.1:5173",
    #     "https://your-production-domain.com",
    # ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class TestMessage(BaseModel):
    texts: List[str]


@app.post("/objectives")
async def get_objectives(data: TestMessage):
    return await gemini.objectives(data.texts)


@app.post("/key-results")
async def get_key_results(data: TestMessage):
    return await gemini.key_results(data.texts)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
