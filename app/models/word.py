from beanie import Document
from pydantic import BaseModel

class Word(Document):
    word: str
    difficulty: int
class Config:
    collection = "words"