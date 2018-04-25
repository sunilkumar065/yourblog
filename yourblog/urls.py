"""yourblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from blog.views import index
from accounts.views import RegistrationView,LoginView,logout_view,PostOfUserView

urlpatterns = [
    url('^$',index),
    url('admin/', admin.site.urls),
    url('blog/',include('blog.urls')),
    url('register',RegistrationView.as_view(),name='register'),
    url('login',LoginView.as_view(),name='login'),
    url('logout',logout_view,name='logout'),
    url(r'(?P<pk>\d+)/myposts',PostOfUserView.as_view(),name='user-posts')
]
