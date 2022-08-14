from django.urls import path
from posts.views import allPostView, singlePostView, newPostView, editPostView, deletPostView



urlpatterns = [
    path('', allPostView, name='urlAllPost'),
    path('/<int:id>', singlePostView, name='urlSinglePost'),
    path('/new', newPostView, name='newPost'),
    
    path('<int:id>/edit', editPostView, name='urlEditPost'),
    path('<int:id>/delete', deletPostView, name='urlDeletPost')
]
