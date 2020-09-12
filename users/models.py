from django.db import models
from django.contrib.auth.models import AbstractUser


class CstUser(AbstractUser):
    def __str__(self):
        return f'Użytkownik CST {self.username} {self.email}'


class Subject(models.Model):
    managing_person = models.ForeignKey(
        to=CstUser, on_delete=models.DO_NOTHING, null=True)


class Person(Subject):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    pesel = models.CharField(max_length=16, null=True)
    foreign_id = models.CharField(max_length=64, null=True)


class Organisation(Subject):
    name = models.CharField(max_length=256)
    kind = models.CharField(max_length=256)
    nip = models.CharField(max_length=16, null=True)
    foreign_id = models.CharField(max_length=64, null=True)
    superior = models.ForeignKey(
        to='Organisation', on_delete=models.DO_NOTHING, null=True)
