# Generated by Django 3.1.1 on 2020-09-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(choices=[('POPC', 'Program Operacyjny Polska Cyfrowa'), ('POIR', 'Program Operacyjny Inteligentny Rozwój'), ('KPOD', 'Krajowy Program Odbudowy'), ('FSTR', 'Fundusz Sprawiedliwej Transformacji')], max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('number', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]