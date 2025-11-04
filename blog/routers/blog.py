from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repositories import blog

router = APIRouter(
    prefix='/blog',
    tags=["blogs"]
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED )
def create(request: schemas.Blog, db : Session = Depends(database.get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    return blog.show(id, response, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    return blog.destroy(id, db)

@router.put("/{id}", status_code= status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request,  db)