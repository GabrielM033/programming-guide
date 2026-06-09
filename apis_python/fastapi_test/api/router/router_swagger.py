from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router_swagger = APIRouter()

@router_swagger.get("/", include_in_schema=False)
def swagger_default():
    
    return RedirectResponse("/docs")
