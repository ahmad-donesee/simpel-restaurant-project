from django.shortcuts import render
from food.models import Food
# Create your views here.

def listmenu(request):
    foods=Food.objects.all()
    context={"foods":foods}
    return render(request,"menu/menu.html",context)