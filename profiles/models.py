from mongoengine import Document
from mongoengine import StringField,EmailField,ListField,DateTimeField
from datetime import datetime

class Profile(Document):
    username = StringField(max_len=10)
    email = EmailField(required=True)
    password = StringField(required=True)
    first_name = StringField(required=True, db_field='fn')
    last_name = StringField(required=True, db_field='ln')
    profession = StringField(db_field='prof')
    description = StringField(db_field='desc')
    topics_of_interest = ListField(StringField(), db_field='toi')
    created_on = DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email

    def is_authenticated(self):
        return True
