from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.

def view_blogdetail(request):
    blogs=Blog.objects.all()
    cate =Category.objects.all()
    tag =Tags.objects.all()
    context={
        "blogs":blogs,
        'cate':cate,
        'tag':tag,
    }
    return render(request,"blog/blog_detail.html",context)


