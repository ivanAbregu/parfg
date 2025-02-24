from ninja import Schema
from decimal import Decimal
from datetime import datetime


class OrderSchema(Schema):
    id: int
    user_id: int
    total_price: Decimal
    status: str
    created_at: datetime


class OrderCreateSchema(Schema):
    total_price: Decimal
    status: str
