from django.db import models
from django.contrib.auth.models import AbstractUser
from dictionaries.models import Pwd
from .enumerations import InstitutionType


class CstUser(AbstractUser):
    def __str__(self):
        return f'Użytkownik CST {self.username} {self.email}'


class Subject(models.Model):
    managing_person = models.ForeignKey(
        to=CstUser, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        try:
            s = self.person
        except Person.DoesNotExist:
            s = self.organisation
        return str(s)


class Person(Subject):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    pesel = models.CharField(max_length=16, null=True)
    foreign_id = models.CharField(max_length=64, null=True)

    def __str__(self):
        person_id = self.pesel or self.foreign_id
        return f'{self.lastname} {person_id}'


class Organisation(Subject):
    name = models.CharField(max_length=256)
    kind = models.CharField(max_length=256)
    nip = models.CharField(max_length=16, null=True)
    foreign_id = models.CharField(max_length=64, null=True)
    superior = models.ForeignKey(
        to='Organisation', on_delete=models.DO_NOTHING,
        null=True, related_name='inferiors')

    def __str__(self):
        organisation_id = self.nip or self.foreign_id
        return f'{self.name} {organisation_id}'


class InstitutionalRole (models.Model):
    maintype = models.CharField(
        max_length=4, choices=InstitutionType.to_tuple())
    pwds = models.ManyToManyField(to=Subject, related_name='pwd_roles')
    subject = models.ForeignKey(to=Subject, related_name='subject_roles',
                                on_delete=models.CASCADE)
    subject_role_pwd_id = models.CharField(max_length=4, default='9999')

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['subject_role_pwd_id', 'pwd', 'subject_id'],
    #                                 name='unique_id_for_subject_in_pwd')
    #     ]
