import motor.motor_asyncio

# TODO: do not hard code the URL for the database
DATABASE_URL = "mongodb://127.0.0.1:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)

database = client.analytics

orders_collection = database.get_collection('orders')
order_lines_collection = database.get_collection('order_lines')
products_collection = database.get_collection('products')
product_promotions_collection = database.get_collection('product_promotions')
promotions_collection = database.get_collection('promotions')
vendor_commissions_collection = database.get_collection('vendor_commissions')
