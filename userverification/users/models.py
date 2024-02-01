
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table='user_login_datas'

    