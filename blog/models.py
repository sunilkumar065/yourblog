from django.db.models import Model,CharField,TextField,PositiveIntegerField,ForeignKey,\
							 CASCADE,ManyToManyField,DateTimeField
from accounts.models import User

class Tag(Model):
	tag = CharField(max_length=100)

	def __str__(self):
		return self.tag

class Post(Model):
	title = CharField(max_length=200)
	content = TextField()
	votes = PositiveIntegerField(default=0)
	created_on = DateTimeField(auto_now_add=True)
	last_edited = DateTimeField(null=True,blank=True)
	tags = ManyToManyField(Tag,related_name='tags',blank=True)
	user = ForeignKey(User,related_name='author',on_delete=CASCADE)

	def __str__(self):
		return self.title

class Comment(Model):
	content = TextField()
	likes = PositiveIntegerField(default=0)
	created_on = DateTimeField(auto_now_add=True)
	post = ForeignKey(Post,related_name='comments',on_delete=CASCADE)
	user = ForeignKey(User,related_name='comment_by',on_delete=CASCADE)

	def __str__(self):
		return self.content
