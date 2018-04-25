from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,GenericAPIView \
					,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from django.http import Http404
from blog.serializers import PostSerializer,PostDetailSerializer,CommentSerializer, \
					TagSerializer
from blog.models import Post,Comment,Tag
from blog.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def index(request):
	return Response({'running':True})

class TagView(ListAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

	def list(self,request):
		queryset = self.get_queryset()
		serializer = TagSerializer(queryset,many=True)
		return Response(serializer.data)

class CommentView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def create(self,request,*args,**kwargs):
		comment = request.data.get('content',None)
		if comment:
			post = Post.objects.get(pk=kwargs.get('pk'))
			Comment.objects.create(content=comment,post=post)
			post_data = PostDetailSerializer(post)
			return Response(post_data.data)

class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def list(self,request,*args,**kwargs):
		queryset = self.get_queryset()
		serializer = PostSerializer(queryset,many=True)
		response = {'posts':[]}
		for data in serializer.data:
			to_append = {'title':'','summary':''}
			to_append.update({'id':data['id'],
							  'title':data['title'],
							  'summary':data['content'][:50],
							  'votes':data['votes']})
			response['posts'].append(to_append)

		return Response(response)

class PostDetailView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer

class PostCreateView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def create(self,request,*args,**kwargs):
		tag_data = request.data.get('tags',None)
		if tag_data:
			request.data.pop('tags')
		post = Post.objects.create(**request.data)
		if tag_data:
			for tag_id in tag_data:
				post.tags.add(Tag.objects.get(pk=tag_id))
		serializer = PostDetailSerializer(post)
		return Response(serializer.data)

class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	lookup_field = 'pk'

	def update(self,request,*args,**kwargs):
		post = self.get_object()
		post.title = request.data.get('title',post.title)
		post.content = request.data.get('content',post.content)
		tag_data = request.data.get('tags',None)
		if tag_data:
			request.data.pop('tags')
			for tag_id in tag_data:
				post.tags.add(Tag.objects.get(pk=tag_id))
		post.last_edited = datetime.now()
		post.save()
		post_data = PostDetailSerializer(post)
		return Response(post_data.data)

	def partial_update(self,request,*args,**kwargs):
		post = self.get_object()
		post.votes = post.votes+1
		post.save()
		post_data = PostDetailSerializer(post)
		return Response(post_data.data)
