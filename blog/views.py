from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#we created a list of dictnories(dummy data) and passed it into context which is a dictnory and passed context
# as third argument which is accessible within home.html, it is the variable 'posts' through which we can access it


def home(request):
    
    return render(request, 'blog/home.html');

def about(request):
    return render(request, 'blog/about.html');