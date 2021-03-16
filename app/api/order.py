from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.db.order import *
from app.schemas.order import *
from app.schemas.utils import (
    ResponseModel,
    ErrorResponseModel
)

order_router = APIRouter()

@order_router.post("/", response_description="Order data added successfully")