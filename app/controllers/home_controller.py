from fastapi import APIRouter
from ..config import config

router = APIRouter(
    tags=["Home"]
)


@router.get("/")
def home():
    response = {
        "service": {
            "project": "Evaluate Server",
            "version": config.API_VER
        },
        "dev": "BaoNQ24",
        "message": "OK"
    }
    return response
