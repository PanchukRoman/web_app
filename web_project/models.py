from django.conf import settings
from django.db import models

class User(models.Model):
    id_user = models.AutoField (primary_key = True)
    initialis = models.CharField(max_length = 40)
    password = models.CharField (max_length = 45)
    e_mail = models.EmailField()
    
class Answer(models.Model):
    id_answer = models.AutoField (primary_key = True)
    count_right = models.IntegerField()
    count_wrong = models.IntegerField()
    user_id = models.ForeignKey (
        'User' ,  on_delete=models.CASCADE,)

class Roles (models.Model):
    id_role = models. AutoField (primary_key = True)
    role_name = models.CharField (max_length = 40)

class Roles_users (models.Model):
    user_id = models. ForeignKey (
        'User', on_delete = models.CASCADE ,)
    role_id = models. ForeignKey (
        'Roles', on_delete = models.CASCADE ,)
