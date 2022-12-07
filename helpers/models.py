from django.db import models


class BusinessObject(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=200)
    modifiedBy = models.CharField(max_length=200)

    class Meta:
        abstract = True
        ordering = ('-createdAt',)
