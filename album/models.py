from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE,default="")
    first_name=models.CharField(max_length=250,null=False,blank=False,default="")
    last_name=models.CharField(max_length=250,null=False,blank=False,default="")
    country=models.CharField(max_length=250,blank=False,null=False)
    location=models.CharField(max_length=250,default="Abia,Nigeria")
    description=models.TextField(null=False,blank=True)
    phone_number=models.CharField(null=True,blank=True,max_length=14,default="+234")
    photo=models.ImageField(blank=False,null=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    @property
    def owner(self):
        return self.user
       