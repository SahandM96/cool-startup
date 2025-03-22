from app.models.color import Color

async def get_all_colors():
    return await Color.find_all().to_list()
