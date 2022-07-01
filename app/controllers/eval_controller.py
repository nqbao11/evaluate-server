from fastapi import APIRouter
from ..config import config
from pydantic import BaseModel
import time
router = APIRouter(
    tags=["Evaluation"]
)


class EvaluationBodyRequest(BaseModel):
    bucket_name: str
    key: str


@router.post("/eval")
async def eval(body: EvaluationBodyRequest):
    return body.bucket_name
