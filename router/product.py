from fastapi import APIRouter, Response, Header, Form
from typing import Optional


router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]




@router.post('/new')
def create_product(name:str = Form(...)):
    products.append(name)
    return products




@router.get("/all")
def get_all_product():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="12345", httponly=True)
    return response


@router.get("/withheader")
def get_products(response: Response, custom_header: Optional[str] = Header(None)):
    return products
