import pymongo

class MongoDB(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient()

    def __enter__(self):
        return self.mongo_client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mongo_client.close()

def insert_msg(msg):
    with MongoDB() as client:
        wx_db = client.wx
        insert_one_result = wx_db.message.insert_one(msg)
        return insert_one_result.acknowledged

def insert_contact(contact):
    with MongoDB() as client:
        wx_db = client.wx
        insert_one_result = wx_db.contact.insert_one(contact)
        return insert_one_result.acknowledged
