from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default="")
    first_name=models.CharField(max_length=250,null=False,blank=False,default="")
    last_name=models.CharField(max_length=250,null=False,blank=False,default="")
    nationality=models.CharField(max_length=250,blank=False,null=False)
    location=models.CharField(max_length=250,default="Abia,Nigeria")
    description=models.TextField(null=False,blank=False)
    phone_number=models.CharField(null=True,blank=True,max_length=15,default="+234")
    photo=models.ImageField(blank=False,null=False)

    def __str__(self):
        return self.first_name
       