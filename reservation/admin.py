from django.contrib import admin
from .models import Reserve
# Register your models here.

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date')
    search_fields=('name','email')
    
    
admin.site.register(Reserve,ReserveAdmin)