from typing import List
from pydantic import BaseModel, ConfigDict



class Article(BaseModel):
    title:str
    content:str
    published:bool
    
    model_config = ConfigDict(from_attributes=True)
    

class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    creator_id:int
    
    
    
    
class User(BaseModel):
    id:int
    username:str
    
        


class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user: User
    
    model_config = ConfigDict(from_attributes=True)
    


class UserBase(BaseModel):
    username:str
    email:str
    password:str
    
    
class UserDisplay(BaseModel):
    username: str
    email:str
    items: List[Article] = []
    
    
    model_config = ConfigDict(from_attributes=True)