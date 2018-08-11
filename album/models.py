from django.db import models


# Create your models here.
class Profile(models.Model):
    full_name=models.CharField(max_length=250,null=False,blank=False, default=" surname  firstname")
    nationality=models.CharField(max_length=250,blank=False,null=False)
    location=models.CharField(max_length=250,default="Abia,Nigeria")
    description=models.TextField(default="Describe the person in simplest way possible",null=False,blank=False)
    phone_number=models.CharField(null=True,blank=True,max_length=15,default="+234")
    photo=models.ImageField(blank=False,null=False)

    def __str__(self):
        return self.full_name
        