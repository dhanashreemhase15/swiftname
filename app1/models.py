from django.db import models

# Create your models here.
class course(models.Model):
    cname=models.CharField(max_length=50)
    cdur=models.IntegerField()
    cprice=models.FloatField()