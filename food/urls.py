from . models import Food
from django.urls import path
from . import views

app_name="food"

urlpatterns=[
    path("",views.food_list,name="food_list"),
    path("<int:id>/",views.food_detail,name="food_detail"),
]