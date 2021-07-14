from django.db import models

# Create your models here.
"""from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)"""

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=8)
    repassword = models.CharField(max_length=8)
