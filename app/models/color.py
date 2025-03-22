from beanie import Document
from pydantic import BaseModel

class Color(Document):
    name: str
    hex: str
class Config:
    collection = "colors"
