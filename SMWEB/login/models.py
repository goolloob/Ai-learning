from django.db import models

# Create your models here.
class User(models.Model):
    pass
    # id int primary_key auto_increment
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.IntegerField()
