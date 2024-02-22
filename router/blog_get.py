from fastapi import APIRouter, status, Response, Depends
from enum import Enum
from router.blog_post import required_functionality
from typing import Optional

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}

@router.get("/all")
def get_blogs(
    page:int=1,
    page_size: Optional[int] = None,
    req_params: dict = Depends(required_functionality),
):
    return {"message": f"All {page_size} blogs on page {page}", "req": req_params}




@router.get(
    "/{id}",
    summary="Retrieve all blocks",
    description="bla bla bla",
)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} is not exist"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id {id}"}


