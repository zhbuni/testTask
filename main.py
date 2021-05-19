from typing import List
from fastapi import FastAPI
from database import database, engine, metadata
from models import languages
import crud
import schemas


metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/languages/", response_model=List[schemas.Language])
async def read_languages():
    query = languages.select()
    return await database.fetch_all(query)


@app.post("/languages/", response_model=schemas.LanguageCreate)
async def create_language(language: schemas.LanguageCreate):
    return await crud.create_language(language=language)


@app.delete("/languages/{language_id}")
async def delete_language(language_id: int):
    query = languages.delete().where(id == language_id)
    await database.execute(query)
    return {"detail": "Language deleted", "status_code": 204}

