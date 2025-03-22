from fastapi import FastAPI
from app.routes import colors, words
app = FastAPI()
app.include_router(colors.router)
app.include_router(words.router)
@app.get("/")
async def root():
    return {"message": "Server is running"}