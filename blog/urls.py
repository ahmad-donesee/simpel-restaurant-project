from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="blog"



urlpatterns=[
    path('',views.blog_view,name="blog_list"),
    path('<int:id>/',views.blog_detail_view,name="blog_detail"),
    # path('<int:id>/<slug:slug>/',views.blog_detail_view,name="blog_detail"),
    
]
