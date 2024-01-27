from django.db import models
from django.utils.translation import gettext as _
# Create your models here.



class Reserve(models.Model):
    name=models.CharField(_("نام و نام خانوادکی"),max_length=30)
    email=models.EmailField(_("ایمیل"),max_length=40)
    phone=models.IntegerField(_("شماره تلفن"))
    number=models.PositiveIntegerField(_("تعداد"))
    date=models.DateField(_("تاریخ"), auto_now=False, auto_now_add=True)
    time=models.TimeField(_("ساعت"),auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="ثبت نام"
        
    