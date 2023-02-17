from django.db import models
class Student(models.Model):
    stupid =models.IntegerField()
    stuname=models.CharField(max_length=70)
    stupas=models.CharField(max_length=70)
    Comment=models.CharField(max_length=40, default='not available')
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
      Token.objects.create(user=instance)  
