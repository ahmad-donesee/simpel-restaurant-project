from django.contrib import admin
from . models import *
# Register your models here.
  
app_name="blog"
  
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date','author']
    search_fields=['title','author']
class CategoyAdmin(admin.ModelAdmin):
    list_display=['title','slug','publish_at']
    search_fields=['title','slug']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoyAdmin)
admin.site.register(Tags)
admin.site.register(Comments)