"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path,include
from blog.views import create_blog_post_view,category_view,tag_view,fav_update_view,post_edit_view

app_name= 'blog'

urlpatterns = [
    path('create/',create_blog_post_view,name='create_blog_post_view' ),
    path('category/<slug:category_slug>/',category_view,name='category_view' ),
    path('tag/<slug:tag_slug>/',tag_view,name='tag_view' ),
    path('post/<slug:post_slug>/edit/',post_edit_view,name='post_edit_view'),
    path('fav-update/',fav_update_view,name='fav_update_view' ),
    
   
]
