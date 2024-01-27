from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

DEFAULT = "abc"

# Create your models here.

class Blog(models.Model):
    title = models.CharField(_('عنوان'), max_length=200)
    date=models.DateTimeField(_("تاریخ"), auto_now=True, auto_now_add=False)
    created_at=models.DateTimeField(_("زمان ایجاد شده"),auto_now=False,default=timezone.now)
    content=models.TextField(_("متن"))
    author=models.ForeignKey(User,verbose_name=_("نویسنده "),on_delete=models.CASCADE)
    discription=models.CharField(_("توضیحات"),max_length=100)
    slug=models.SlugField(_("سؤی وبگاه"))
    image=models.ImageField(_("عکسها"), upload_to="blogs/", height_field=None, width_field=None, max_length=None)
    category=models.ForeignKey("Category",verbose_name=_("دسته بندی"),on_delete=models.CASCADE,related_name="Blog")
    tag=models.ForeignKey("Tags",verbose_name=_("تگها"),on_delete=models.CASCADE,related_name="Blog")

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.id])
    
    
    class Meta:
        verbose_name_plural="بلاگ"
    def __str__(self):
        return self.title

    
class Category(models.Model):
    title=models.CharField(_("عنوان"),max_length=200,blank=True,null=True)
    slug=models.SlugField(_("سيوی  سایت"),blank=True,null=True)
    publish_at=models.DateTimeField(_("انتشار"), auto_now=False, auto_now_add=False,blank=True,null=True)
    
    # def get_absolute_url(self):
    #     return reverse("blog:blog_detail", args=[self.id])
    
    
    class Meta:
        verbose_name_plural="دسته بندیها"
        
    def __str__(self):
        return self.title
    
    
class Tags(models.Model):
    title=models.CharField(_("عنوان"),max_length=200)
    slug=models.SlugField(_("عنوان لاتین"))
    publish_at=models.DateTimeField(_("تاریخ انتشار"),auto_now=True,auto_now_add=False)
    update_at=models.DateTimeField(_("تاریخ به روز رسانی"),auto_now=True,auto_now_add=False)

    # def get_absolute_url(self):
    #     return reverse("blog:blog_detail", args=[self.id])

    
    class Meta:
        verbose_name_plural="تگها"

    
    def __str__(self):
        return self.title

class Comments(models.Model):
    name=models.CharField(_("نام"),max_length=50)
    email=models.EmailField(_("پست الکترونیکی"),max_length=75)
    message=models.TextField(_("نظر"))
    date=models.DateField(_("تاریخ انتشار"), auto_now=True, auto_now_add=False)
    blog=models.ForeignKey("Blog",verbose_name=" مقاله مربوطه ",related_name='Comments',on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.id])
    
    class Meta:
        verbose_name_plural="نظرات"

    
    def __str__(self):
        return self.name
    







