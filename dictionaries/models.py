from django.db import models
import dictionaries.enumerations as enums


class Dictionary(models.Model):
    class Meta:
        abstract = True


class Axis(Dictionary):
    programme = models.CharField(
        max_length=500, choices=enums.Programme.choices())
    name = models.CharField(max_length=500)
    number = models.SmallIntegerField()

    def __str__(self):
        return f'{self.programme}.Oś {self.number}.{self.name}'

    class Meta:
        ordering = ['programme', 'number']


class Measure(Dictionary):
    axis = models.ForeignKey(
        to=Axis, on_delete=models.CASCADE, related_name='measures')
    name = models.CharField(max_length=500)
    number = models.SmallIntegerField()

    def __str__(self):
        return f'{self.axis.programme}.Oś {self.axis.number}.Działanie {self.number}.{self.name}'

    class Meta:
        ordering = ['axis', 'number']


class Institution (Dictionary):
    name = models.CharField(max_length=500)
    vat_number = models.CharField(max_length=10)
