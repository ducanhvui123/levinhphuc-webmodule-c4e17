from mongoengine import *

class Customer(Document):
    name = StringField()
    yob = IntField()
    height = IntField()
    gender = IntField()
    address = StringField()
    status = BooleanField()
    age = IntField()
    phone = StringField()
