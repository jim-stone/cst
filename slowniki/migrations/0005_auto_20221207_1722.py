# Generated by Django 3.1.1 on 2022-12-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slowniki', '0004_auto_20220122_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'ordering': ('-createdAt',)},
        ),
        migrations.AlterModelOptions(
            name='dictionaryentry',
            options={'ordering': ('-createdAt',)},
        ),
        migrations.AlterModelOptions(
            name='dictionaryvalues',
            options={'ordering': ('-createdAt',)},
        ),
        migrations.AlterModelOptions(
            name='entryfieldspecification',
            options={'ordering': ('-createdAt',)},
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
