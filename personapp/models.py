from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()
class person(models.Model):
 	name = models.CharField(verbose_name= 'name',db_index=True,max_length=64)
 	adress = models.CharField(verbose_name= 'adress',db_index=True,max_length=64)
 	work = models.CharField(verbose_name= 'work',db_index=True,max_length=64)
 	age = models.IntegerField(verbose_name='age')
