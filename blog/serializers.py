from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from blog.models import Comment,Post

class CommentSerializer(EmbeddedDocumentSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class PostListSerializer(DocumentSerializer):
	class Meta:
		model = Post
		fields = '__all__'