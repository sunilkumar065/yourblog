from mongoengine import Document,EmbeddedDocument, StringField,IntField,DateTimeField,\
						ListField,EmbeddedDocumentField
from datetime import datetime

class Comment(EmbeddedDocument):
	content = StringField()
	likes = IntField(default=0)

class Post(Document):
	title = StringField()
	content = StringField()
	votes = IntField(default=0)
	posted_on = DateTimeField(default=datetime.now())
	last_edited = DateTimeField()
	comments = ListField(EmbeddedDocumentField(Comment))
	tags = ListField()
