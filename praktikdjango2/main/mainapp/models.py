from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = "username"

    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()

    def __str__(self):
        return self.username


class Note(models.Model):
    content = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)


    def add(self, content, user_id_id):
        self.content = content
        self.user_id_id = user_id_id
        self.save()

    def __str__(self):
        return self.content
