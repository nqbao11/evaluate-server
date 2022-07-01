import imp
"""
Evaluate Server API controller
"""

from fastapi import FastAPI, APIRouter
from .controllers import home_controller, eval_controller
from .config import config

router = APIRouter()

# ADD route to router
router.include_router(home_controller.router)
router.include_router(eval_controller.router)
##

app = FastAPI(
    title="Evaluate Server",
    version=config.API_VER
)

app.include_router(router)
