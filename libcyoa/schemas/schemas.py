from typing import Sequence
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    id: int
    hash: str

class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl  # 3

class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]  # 4

class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int