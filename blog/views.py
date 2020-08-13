from django.shortcuts import render
from .models import Blog


# Create your views here.
def all_blog(request):
    blogs = Blog.objects.all()
    all_blogData = {'blogs':blogs}
    return render(request, 'blog/all_blog.html', all_blogData)



def view_blog(request, bid):
    viewblog = Blog.objects.filter(pk=bid)
    viewblogData = {'viewblog':viewblog}
    return render(request, 'blog/view_blog.html', viewblogData)