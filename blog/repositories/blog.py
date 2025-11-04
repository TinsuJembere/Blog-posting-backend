from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db : Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail' : f'blog with the id {id} is not available'}
    return blog

def destroy(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    existing_blog = blog_query.first()
    
    if not existing_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
    
    return {"detail": "deleted successfully"}

def update(id: int, request: schemas.Blog, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return blog_query.first()