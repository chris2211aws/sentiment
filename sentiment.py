from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentInput(BaseModel):
    text: str

@app.post("/sentiment/")
async def analyze_sentiment(input: SentimentInput):
    # Analyze sentiment
    blob = TextBlob(input.text)
    sentiment_score = blob.sentiment.polarity  # Range: -1 to 1

    # Convert polarity to a score from 1 to 10
    if sentiment_score < 0:
        score = max(1, int((sentiment_score + 1) * 5))  # Map -1 to 1
    else:
        score = min(10, int((sentiment_score) * 10))  # Map 1 to 10

    return {"score": score + 500}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
