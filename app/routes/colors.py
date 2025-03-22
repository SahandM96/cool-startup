from fastapi import APIRouter
from app.models.color import Color

router = APIRouter(prefix="/colors")
@router.post("/")
async def add_color(color: Color):
    await color.insert()
    return {"message": "Color added"}