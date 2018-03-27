from django.conf.urls import url
from blog.views import PostListView,PostCreateView

urlpatterns = [
	url(r'^$',PostListView.as_view(),name='show-all'),
	url(r'^create',PostCreateView.as_view(),name='create-post'),
]