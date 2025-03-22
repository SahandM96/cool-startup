from app.models.word import Word

async def get_all_words():
    return await Word.find_all().to_list()