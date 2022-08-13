from django.shortcuts import render
from .models import postModel
from .forms import postForm

# Create your views here.

def allPostView(request):
    posts = postModel.objects.all()
    return render(request, 'allPost.html', {'allPosTemp' : posts})

def singlePostView(request, id):
    posts = postModel.objects.get(id=id)
    return render(request, 'singlePost.html', {'sinPosTemp' : posts})

def newPostView(request):
    if request.method == 'post':
        form = postForm(request.post)
        if form.is_valid():
            form.save()
    else:
        form = postForm()
    return render(request, 'newPost.html', {'forms' : form})

def editPostView(request, id):
    pass

def deletPostView(request, id):
    pass
