from django.urls import path
from . import views
app_name="blogdetail"

urlpatterns=[
    path('',views.view_blogdetail,name="blogdetail")
    #path('',views.index,name='index'),
]