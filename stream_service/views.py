from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def sample_viewpage(request):
    return render(request, "view.html")
