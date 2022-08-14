from django.shortcuts import render, redirect
from .models import postModel
from .forms import postForm

# Create your views here.
# CRUD opration: Create , Retrive , Update , Delete

def allPostView(request): # ---> Retrive
    posts = postModel.objects.all()
    return render(request, 'allPost.html', {'allPosTemp' : posts})

def singlePostView(request, id):
    posts = postModel.objects.get(id=id)
    return render(request, 'singlePost.html', {'sinPosTemp' : posts})

def newPostView(request): # ------> Create
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = postForm()
    return render(request, 'newPost.html', {'forms' : form})

def editPostView(request, id): # -----> Update
    posts = postModel.objects.get(id=id)    
    if request.method == 'POST':
        form = postForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
    else:
        form = postForm(instance=posts)
    return render(request, 'editPost.html', {'forms' : form})

def deletPostView(request, id): # -----> Delete
    posts = postModel.objects.get(id=id)    
    posts.delete()
    return redirect('/blog/')
    
 