from sqlalchemy import Column, Integer, String, Table
from database import metadata


languages = Table(
    "languages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, index=True),
    Column("code", String)
)
