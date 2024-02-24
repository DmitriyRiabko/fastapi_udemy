from fastapi import APIRouter, Depends, Response, status, File, UploadFile
import shutil

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {"lines": lines}


@router.post("/uploadfile")
def get_uploadfile(upload_file: UploadFile = File(...)):
    
    path = f'files/{upload_file.filename}'
    
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
        
        
    
    return{
        'filename':upload_file.filename,
        'type':upload_file.content_type,
        'file':upload_file.headers
        
    }
