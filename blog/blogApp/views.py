from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    # request is handled using HttpResponse object
    #return HttpResponse("<h1> home </h1>")
    return render(request,'index.html')


def blog_post(request):
    # request is handled using HttpResponse object
    #return HttpResponse("<h1> home </h1>")
    return render(request,'blog-post-1.html')
