from django.db import models
# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=80)
    cam = models.CharField(max_length=100)
class email(models.Model):
    contact_id  = models.IntegerField()
# contact.objects.filter(client=id).order_by('-id')
# con = contact.objects.order_by('-id')