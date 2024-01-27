from django.contrib import admin
from .models import Food
# Register your models here.
# @admin.register(Food)
class AdminFood(admin.ModelAdmin):
    list_display=['name','rate','price'] 
    search_fields=['name']
    # list_display_links=['price']
    
# admin.site.register(Food)
admin.site.register(Food,AdminFood)
