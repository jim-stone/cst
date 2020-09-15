# Generated by Django 3.1.1 on 2020-09-15 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='superior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='inferiors', to='users.organisation'),
        ),
        migrations.CreateModel(
            name='InstitutionalRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintype', models.CharField(choices=[('KOOR', 'Koordynująca'), ('WDRA', 'Wdrażająca'), ('BENE', 'Beneficjent')], max_length=4)),
                ('subject_role_pwd_id', models.CharField(default='9999', max_length=4)),
                ('pwd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='i_roles', to='dictionaries.pwd')),
                ('subject', models.ManyToManyField(related_name='i_roles', to='users.Subject')),
            ],
        ),
    ]