from django.db import models
from helpers.models import BusinessObject


class Dictionary(BusinessObject, models.Model):
    name = models.CharField(max_length=200, unique=True)
    isHorizontal = models.BooleanField()
    isModifiable = models.BooleanField()
    isExtensible = models.BooleanField()

    def __str__(self):
        return self.name


class EntryFieldSpecification(BusinessObject, models.Model):
    dictionaryId = models.ForeignKey(
        Dictionary, related_name='field_specs', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=2000)
    type = models.PositiveSmallIntegerField()
    isReference = models.BooleanField()
    ReferencedDict = models.ForeignKey(
        Dictionary, related_name='referencing_fields', on_delete=models.PROTECT,
        null=True, blank=True)
    isUnique = models.BooleanField(default=False)
    uniqueGroupNumber = models.PositiveSmallIntegerField(
        null=True, default=None)
    defaultValue = models.CharField(max_length=2000, null=True, default=None)
    isOptional = models.BooleanField(default=False)


class DictionaryEntry(BusinessObject, models.Model):
    dictionaryId = models.ForeignKey(
        Dictionary, related_name="entries", on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    valuesAsJSON = models.JSONField()
    displayValue = models.CharField(max_length=2000, null=True)


class DictionaryValues (BusinessObject, models.Model):
    name = models.CharField(max_length=2000)
    value = models.CharField(max_length=2000)
    type = models.PositiveSmallIntegerField()
    isUnique = models.BooleanField()
    dictionaryEntry = models.ForeignKey(
        DictionaryEntry, related_name='field_values', on_delete=models.CASCADE)
    referencedValue = models.ForeignKey(
        'DictionaryValues', on_delete=models.PROTECT, null=True)
