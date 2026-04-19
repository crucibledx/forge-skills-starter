from datetime import datetime

from pydantic import BaseModel, HttpUrl


class TagBase(BaseModel):
    name: str


class TagResponse(TagBase):
    id: int

    class Config:
        from_attributes = True


class BookmarkCreate(BaseModel):
    url: HttpUrl
    title: str
    description: str = ""
    tags: list[str] = []


class BookmarkUpdate(BaseModel):
    url: HttpUrl | None = None
    title: str | None = None
    description: str | None = None
    tags: list[str] | None = None


class BookmarkResponse(BaseModel):
    id: int
    url: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True
