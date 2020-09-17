from django.db import models
# import dictionaries.enumerations as enums


class Dictionary(models.Model):
    class Meta:
        abstract = True


class Pwd(Dictionary):

    def __str__(self):
        try:
            p = self.programme
        except Programme.DoesNotExist:
            try:
                p = self.axis
            except Axis.DoesNotExist:
                p = self.measure
        return str(p)


class Programme(Pwd):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.code}.{self.name}'

    class Meta:
        ordering = ['code']


class Axis(Pwd):
    prog = models.ForeignKey(
        to=Programme, on_delete=models.CASCADE, related_name='axes')
    name = models.CharField(max_length=500)
    number = models.SmallIntegerField()

    def __str__(self):
        return f'{self.prog}.Oś {self.number}.{self.name}'

    class Meta:
        ordering = ['prog', 'number']


class Measure(Pwd):
    ax = models.ForeignKey(
        to=Axis, on_delete=models.CASCADE, related_name='measures')
    name = models.CharField(max_length=500)
    number = models.SmallIntegerField()

    def __str__(self):
        return f'{self.ax.prog}.Oś {self.ax.number}.Działanie {self.number}.{self.name}'

    class Meta:
        ordering = ['ax', 'number']
