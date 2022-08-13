from django.shortcuts import render
from .models import postModel

# Create your views here.

def allPostView(request):
    posts = postModel.objects.all()
    return render(request, 'allPost.html', {'allPosTemp' : posts})

def singlePostView(request, id):
    posts = postModel.objects.get(id=id)
    return render(request, 'singlePost.html', {'sinPosTemp' : posts})

def newPostView(request):
    pass

def editPostView(request, id):
    pass

def deletPostView(request, id):
    pass
