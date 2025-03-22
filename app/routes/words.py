from fastapi import APIRouter
from app.models.word import Word
router = APIRouter(prefix="/words")
@router.post("/")
async def add_word(word: Word):
    await word.insert()
    return {"message": "Word added"}