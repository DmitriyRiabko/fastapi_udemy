from fastapi import APIRouter, Response, Header, Form
from typing import Optional
from custom_log import log
import time

router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]





async def time_consuming_functionality():
    time.sleep(5)
    return 'ok'




@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products


@router.get("/all")
async def get_all_product():
    await time_consuming_functionality()
    log("MyAPI", "call get all products")
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="12345", httponly=True)
    return response


@router.get("/withheader")
def get_products(response: Response, custom_header: Optional[str] = Header(None)):
    return products
