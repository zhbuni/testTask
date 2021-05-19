from database import database
from models import languages
import schemas


async def get_languages(skip: int = 0, limit: int = 100):
    query = languages.select().offset(skip).limit(limit)
    results = await database.fetch_all(query)
    return [dict(result) for result in results]


async def create_language(language: schemas.LanguageCreate):
    query = languages.insert().values(name=language.name, code=language.code)
    last_language_id = await database.execute(query)
    return {**language.dict(), "id": last_language_id}

