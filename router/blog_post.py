from typing import List, Dict
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url:str
    alias:str


class BlogModel(BaseModel):
    title: str
    content: str
    published: bool | None
    tags:List[str] = []
    metadata:Dict[str,str] = {'key':'value'}
    image:Image  | None = None

    pass


@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}
    ...


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(None, title="ID of comment", description="Some descr"),
    content: str = Body("Hi"),
    v: List[str | None]  = Query(None),
):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id,
        "content": content,
        "version": v,
    }



def required_functionality():
    return {'message':'Learning is important'}