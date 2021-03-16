from bson.objectid import ObjectId

from app.db.db import orders_collection

__all__ = ["retrieve_orders", "retrieve_order", "add_order"]


def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "created_at": order["created_at"],
        "vendor_id": order["vendor_id"]
    }


# retrieve moves from the database
async def retrieve_orders():
    orders = []
    async for order in orders_collection.find():
        orders.append(order_helper(order))
    return orders


# retrieve a move by the ID
async def retrieve_order(id: str) -> dict:
    order = await orders_collection.find_one({"_id": ObjectId(id)})
    if order:
        return order_helper(order)


# add a move to the database
async def add_order(order: dict) -> dict:
    order = await orders_collection.insert_one(order)
    new_order = await orders_collection.find_one({"_id": ObjectId(order.inserted_id)})

    return order_helper(new_order)
