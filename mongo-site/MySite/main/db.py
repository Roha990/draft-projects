import pymongo
from django.conf import settings
from bson.objectid import ObjectId

client = pymongo.MongoClient(settings.MONGO_URL)
db = client.main


def get_products():
    products = list(db.products.find())
    new_products = [{'id': product['_id'], "Name": product['Name'], "Amount": product['Amount']} for product in
                    products]
    return new_products


def get_info_product(product_id):
    my_product = db.products.find_one({'_id': ObjectId(product_id)})
    return my_product['Name'], list(my_product.keys())[1:], list(my_product.values())[1:]


def get_product_name(product_id):
    my_product = db.products.find_one({"_id": ObjectId(product_id)})
    return my_product['Name']


def add_field(product_id, new_field, new_value):
    db.products.update_one({"_id": ObjectId(product_id)}, {"$set": {new_field: new_value}})


def delete_field(product_id, field_name):
    db.products.update_one({"_id": ObjectId(product_id)}, {"$unset": {field_name: ""}})


def add_product(fields):
    db.products.insert_one(fields)


def delete_product(product_id):
    db.products.delete_one({"_id": ObjectId(product_id)})
