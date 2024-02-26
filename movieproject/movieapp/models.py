from django.db import models

# Create your models here.


class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    certified_by=models.CharField(max_length=200,null=True)
    

class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null = True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/',null=True)
    censor_details=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    # can use foreignkey for one to many relation
    # many to many field
    def __str__(self) :
        return self.title

