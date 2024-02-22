from fastapi import FastAPI, status, Response
from contextlib import asynccontextmanager
from router import blog_get
from router import blog_post

@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # end


app = FastAPI(title="practise", lifespan=lifespan)
app.include_router(blog_get.router)
app.include_router(blog_post.router)



@app.get("/hello")
async def root():
    return {"message": "Hello Udemy"}



