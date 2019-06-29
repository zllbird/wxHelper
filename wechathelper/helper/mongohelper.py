import pymongo

class MongoDB(object):
    def __init__(self):
        self.mongo_client = pymongo.MongoClient()

    def __enter__(self):
        return self.mongo_client.wx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mongo_client.close()

def insert_msg(msg):
    with MongoDB() as wx_db:
        insert_one_result = wx_db.message.insert_one(msg)
        return insert_one_result.acknowledged

def insert_contact(contact):
    with MongoDB() as wx_db:
        insert_one_result = wx_db.contact.insert_one(contact)
        return insert_one_result.acknowledged

def find_msg(msgId):
    with MongoDB() as wx_db:
        msg = wx_db.message.find_one({'msgId': msgId})
        return msg

def find_friend(remarkName):
    with MongoDB() as wx_db:
        msg = wx_db.contact.find_one({'remarkName': remarkName})
        return msg

def save_text(text):
    with MongoDB() as wx_db:
        text_msg = wx_db.textMsg.insert_one(text)
        return text_msg

def find_text_to_friend():
    with MongoDB() as wx_db:
        text_msg = wx_db.textMsg.find_one()
        return text_msg

def save_image(image):
    with MongoDB() as wx_db:
        text_msg = wx_db.imageMsg.insert_one(image)
        return text_msg

def find_image_to_friend():
    with MongoDB() as wx_db:
        image_msg = wx_db.imageMsg.find_one()
        return image_msg