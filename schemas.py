from pydantic import BaseModel


class LanguageBase(BaseModel):
    name: str
    code: str = None


class LanguageCreate(LanguageBase):
    pass


class Language(BaseModel):
    id: int

    class Config:
        orm_mode = True
