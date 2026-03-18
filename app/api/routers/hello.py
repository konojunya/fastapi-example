from fastapi import APIRouter

from app.services.hello_service import HelloService
from app.schemas.hello import HelloResponse

router = APIRouter()

@router.get("/", status_code=200, response_model=HelloResponse)
async def hello_world():
    service = HelloService()
    return service.get_message()