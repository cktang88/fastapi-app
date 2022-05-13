from typing import Optional

from sqlmodel import Field, SQLModel


class SongBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None


class Song(SongBase, table=True):  # type: ignore
    id: int = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass
