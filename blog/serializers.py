from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework.serializers import Serializer
from blog.models import Post,Comment
from datetime import datetime

class CommentSerializer(DocumentSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class PostListSerializer(DocumentSerializer):
	comments = CommentSerializer(many=True)

	class Meta:
		fields = ('title','content','votes','posted_on','last_edited','tags','comments')

class PostCreateSerializer(DocumentSerializer):
	comments = CommentSerializer(many=True,required=False)

	class Meta:
		model = Post
		fields = ('title','content','tags','comments')

	def create(self,validated_data):
		comments_data = validated_data.get('comments',None)
		if comments_data:
			validated_data.pop("comments")
		post = Post.objects.create(**validated_data)
		if comments_data:
			comment = CommentSerializer(many=True,data=comments_data)
			if comment.is_valid():
				for comment in comments_data:
					Comment.objects.create(content=comment['content'],post=post)
		return post

	def update(self,instance,validated_data):
		comments = validated_data.pop('comments')
		updated_instance = super(PostSerializer,self).update(instance,validated_data)
		updated_instance.last_edited = datetime.now()
		for cmnt in comments:
			updated_instance.comments.append(Comment(**cmnt))
		updated_instance.save()
		return updated_instance
