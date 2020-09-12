from django.db import models
from django.contrib.auth.models import AbstractUser


class CstUser(AbstractUser):
    # user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Użytkownik CST {self.username} {self.email}'
