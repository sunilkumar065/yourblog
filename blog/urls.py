from django.conf.urls import url
from blog.views import IndexView,PostListView,PostCreateView,PostUpdateDeleteView

urlpatterns = [
    url(r'^view/?$',PostListView.as_view(),name='view-all'),
    url(r'^create/?$',PostCreateView.as_view(),name='create-post'),
    url(r'^view/(?P<pk>\d+)$',PostListView.as_view(),name='view-one'),
    url(r'^update/(?P<pk>\d+)$',PostUpdateDeleteView.as_view(),name='update-post'),
    url(r'^delete/(?P<pk>\d+)$',PostUpdateDeleteView.as_view(),name='delete-post')
]
