from pydantic import BaseModel


# Shared properties
class OrderLineBase(BaseModel):
    order_id: int
    product_id: int
    product_description: str
    product_price: float
    product_vat_rate: float
    discount_rate: float
    quantity: int
    full_price_amount: float
    discounted_amount: float
    vat_amount: float
    total_amount: float


# Properties to receive on item creation
class OrderLineCreate(OrderLineBase):
    id: int


# Properties to receive on item update
class OrderLineUpdate(OrderLineBase):
    pass


# Properties shared by models stored in DB
class OrderLineInDBBase(OrderLineBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class OrderLine(OrderLineInDBBase):
    pass


# Properties stored in DB
class OrderLineInDB(OrderLineInDBBase):
    pass
