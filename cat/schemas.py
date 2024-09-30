from uuid import UUID

from pydantic import BaseModel


class CatSchema(BaseModel):
    """
    Cat schema.
    """
    id: UUID
    color: str
    age: int
    breed: str
    description: str


class CreateCatRequestSchema(BaseModel):
    """
    Create cat request schema.
    """
    color: str
    age: int
    breed: str
    description: str


class CreateCatResponseSchema(BaseModel):
    """
    Create cat response schema.
    """
    id: UUID
    color: str
    age: int
    breed: str
    description: str


class UpdateCatRequestSchema(BaseModel):
    """
    Update cat request schema.
    """
    color: str | None = None
    age: int | None = None
    breed: str | None = None
    description: str | None = None


class UpdateCatResponseSchema(BaseModel):
    """
    Update cat response schema.
    """
    id: UUID
    color: str
    age: int
    breed: str
    description: str


class CatsBreedSchema(BaseModel):
    breeds: list[str]
