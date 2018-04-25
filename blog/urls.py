from django.conf.urls import url
from blog.views import PostListView,PostCreateView,PostUpdateDeleteView, \
                PostDetailView,CommentView,TagView

urlpatterns = [
    url(r'^view/?$',PostListView.as_view(),name='view-all'), #GET
    url(r'^create/?$',PostCreateView.as_view(),name='create-post'), #POST
    url(r'^(?P<pk>\d+)$',PostDetailView.as_view(),name='view-one'), #GET
    url(r'^(?P<pk>\d+)/update$',PostUpdateDeleteView.as_view(),name='update-post'),#PUT
    url(r'^(?P<pk>\d+)/delete$',PostUpdateDeleteView.as_view(),name='delete-post'), #DELETE
    url(r'^(?P<pk>\d+)/comment$',CommentView.as_view(),name='comment-on-post'), #POST
    url(r'^(?P<pk>\d+)/vote',PostUpdateDeleteView.as_view(),name='vote-post'), #PATCH
    url(r'^tag$',TagView.as_view(),name='list-tag'), #GET
]
