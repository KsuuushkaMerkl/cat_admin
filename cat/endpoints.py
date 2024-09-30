from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import scoped_session

from cat.models import Cat
from cat.schemas import CatSchema, CreateCatRequestSchema, CreateCatResponseSchema, UpdateCatRequestSchema, \
    UpdateCatResponseSchema, CatsBreedSchema
from core.database import get_session

router = APIRouter()


@router.post('/', response_model=CreateCatResponseSchema)
async def create_cat(
        data: CreateCatRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Create new cat.
    """
    cat = Cat(**data.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@router.patch('/{cat_id}', response_model=UpdateCatResponseSchema)
async def update_cat(
        cat_id: UUID,
        data: UpdateCatRequestSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Update cat.
    """
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        return HTTPException(
            status_code=404,
            detail="Cat not found."
        )
    obj_data = jsonable_encoder(cat)  # noqa
    update_data = data.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(cat, field, update_data[field])
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@router.get('/', response_model=list[CatSchema])
async def get_all_cats(
        db: scoped_session = Depends(get_session)
):
    """
    Get all cat.
    """
    return db.query(Cat).all()


@router.get('/{cat_id}', response_model=CatSchema)
async def get_cat_by_id(
        cat_id: UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Get cat by id.
    """
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if not cat:
        return HTTPException(
            status_code=404,
            detail="Cat not found."
        )
    return cat


@router.delete('/{cat_id}')
async def delete_cat(
        cat_id: UUID,
        db: scoped_session = Depends(get_session)
):
    """
    Delete cat.
    """
    note = db.query(Cat).filter(Cat.id == cat_id).delete()
    if note == 0:
        return HTTPException(
            status_code=404,
            detail="Cat not found."
        )
    return cat_id


@router.post('/search_by_breed', response_model=list[CatSchema])
async def get_cat_by_breed(
        data: CatsBreedSchema,
        db: scoped_session = Depends(get_session)
):
    """
    Get cat by breed.
    """
    return db.query(Cat).filter(Cat.breed.any(*data.breed)).all()
