from pydantic import BaseModel


# Shared properties
class OrderBase(BaseModel):
    vendor_id: int
    customer_id: int


# Properties to receive on item creation
class OrderCreate(OrderBase):
    created_at: str


# Properties to receive on item update
class OrderUpdate(OrderBase):
    pass


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
