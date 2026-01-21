import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

model_name = os.getenv("MODEL_NAME", "microsoft/phi-2")
pipe = pipeline("text-generation", model=model_name, device_map="auto")

class Query(BaseModel):
    prompt: str
    max_length: int = 200

@app.post("/ask")
async def ask_opsgpt(query: Query):
    results = pipe(query.prompt, max_length=query.max_length, truncation=True)
    return {"response": results[0]["generated_text"]}

@app.get("/health")
async def health():
    return {"status": "up"}