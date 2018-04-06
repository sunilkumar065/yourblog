from django.db.models import Model,CharField,TextField,IntegerField,ForeignKey,\
							 CASCADE,ManyToManyField,DateTimeField
from datetime import datetime

class Post(Model):
	title = CharField(max_length=200)
	content = TextField()
	votes = IntegerField(default=0)
	created_on = DateTimeField(auto_now_add=True)
	last_edited = DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Comment(Model):
	content = TextField()
	likes = IntegerField(default=0)
	created_on = DateTimeField(auto_now_add=True)
	post = ForeignKey(Post,on_delete=CASCADE,related_name='comments')

	def __str__(self):
		return self.content

class Tag(Model):
	tag = CharField(max_length=100)
	description = TextField(blank=True)
	post = ManyToManyField(Post,related_name='tags')

	def __str__(self):
		return self.tag
