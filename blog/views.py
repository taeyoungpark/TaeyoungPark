from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def post_detail(request):
        return render(request, 'blog/post_detail.html')

def post_edit(request):
    return render(request, 'blog/post_edit.html')
