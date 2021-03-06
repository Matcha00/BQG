import datetime

from peewee import *
import DBHelp

db = DBHelp()
db.openDB()

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
