from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.


class Food(models.Model):
    FOOD_TYPE=[('drinks',"نوشیدنی ها"),("lunch","ناهار"),("dinner","شام")]
    
    
    name = models.CharField(_("نام غذا"),max_length=20)
    discription=models.CharField(_("توضیحات"), max_length=100)
    rate=models.IntegerField(_("امتیاز"))
    price=models.IntegerField(_("قیمت"))
    time=models.IntegerField(_("زمان لازم"))
    pub_date=models.DateField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    photo=models.ImageField(_("عکس"), upload_to='food', height_field=None, width_field=None, max_length=None)
    tye_food=models.CharField(_("نوع غذا"),choices=FOOD_TYPE,max_length=50,default="drinks")
    
    def get_absolute_url(self):
        return reverse("food:food_detail", args=[self.id])
    
    
    class Meta:
        verbose_name_plural="غداها"
    def __str__(self):
        return self.name
    