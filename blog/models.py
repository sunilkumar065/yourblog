from mongoengine import Document, StringField,IntField,DateTimeField,\
						ListField,ReferenceField,CASCADE
from datetime import datetime

class Post(Document):
	title = StringField()
	content = StringField()
	votes = IntField(default=0)
	posted_on = DateTimeField(default=datetime.now())
	last_edited = DateTimeField()
	tags = ListField(StringField())

class Comment(Document):
	content = StringField()
	likes = IntField(default=0)
	post = ReferenceField(Post,reverse_delete_rule=CASCADE)
	created_on = DateTimeField(default=datetime.now())
