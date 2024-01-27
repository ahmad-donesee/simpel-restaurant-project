from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.


def food_list(request):
    foods=Food.objects.all()
    context={"foods":foods}
    return render(request,"food/list.html",context)

def food_detail(request,id):
    food=Food.objects.get(id=id)
    context={
        "food":food,
    }
    return render(request,"food/detail.html",context)

    
