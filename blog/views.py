from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import *
from . forms import *
from django.http import HttpRequest
from django.http.response import HttpResponsePermanentRedirect
from django.views.generic import DetailView
# Create your views here.



def blog_view(request):
    blog=Blog.objects.all()
    context={
        "blog":blog,
    }
    return render(request,"blog/blog.html",context)


def blog_detail_view(request,id):
    blogs=Blog.objects.get(id=id)
    tags=Tags.objects.all().filter(Blog=blogs)
    # tags=Tags.objects.all().filter(blog=blogs)
    cate=Category.objects.all()
    comments=Comments.objects.all().filter(blog=blogs)
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('blog:blog_list')
    else:
        form=CommentForm()
    context={
        "blogs":blogs,
        "form":form,
        "comments":comments,
        'tags':tags,
        'cate':cate,
        
    }
    return render(request,"blog/blog_detail.html",context)



 # else:
    #     form=CommentForm()
# form=CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=CommentForm()

# if form.is_valid():
#             new_name=form.cleaned_data['name']
#             new_email=form.cleaned_data['email']
#             new_date=form.cleaned_data['date']
#             new_message=form.cleaned_data['message']
#             new_comments=Comments(new_name,new_email,new_date,new_message)
#             new_comments.save()

# new_name=form.cleaned_data['name']
#             new_email=form.cleaned_data['email']
#             new_message=form.cleaned_data['message']
#             new_date=form.cleaned_data['date']
#             new_comments=Comments(blog=blogs,name=new_name,date=new_date,email=new_email,message=new_message)
#             form=new_comments.save()