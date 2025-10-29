from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'page':"hello"}

@app.get("/about")
def about():
    return {'page':"about"}

@app.get('/blog/unpublished')
#to get unpublished blog pages
def blog():
    return {'blog': "unpublished"}

@app.get('/blog')
#to get dynamic blog pages
def blog(limit = 10, published: bool = False, sort: Optional[str] = None):
    if published == True:
        return {'blog': f'{limit} published blogs from the db'}
    else:
         return {'blog': f'{limit} blogs from the db'}

@app.get("/blog/{id}/comments")
def comments(id):
    return {'comments':id + ' comments'}


class Blog(BaseModel):
    title : str
    body: Optional[str]
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return f"blog is created with title as {request.title}"

#changing port number
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.01", port=9000)