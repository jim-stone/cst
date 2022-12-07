# Generated by Django 3.1.1 on 2022-01-22 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slowniki', '0003_dictionaryentry_dictionaryvalues_entryfieldspecification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='dictionary',
            old_name='created_by',
            new_name='createdBy',
        ),
        migrations.RenameField(
            model_name='dictionary',
            old_name='modified_at',
            new_name='modifiedAt',
        ),
        migrations.RenameField(
            model_name='dictionary',
            old_name='modified_by',
            new_name='modifiedBy',
        ),
        migrations.RenameField(
            model_name='dictionaryentry',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='dictionaryentry',
            old_name='created_by',
            new_name='createdBy',
        ),
        migrations.RenameField(
            model_name='dictionaryentry',
            old_name='modified_at',
            new_name='modifiedAt',
        ),
        migrations.RenameField(
            model_name='dictionaryentry',
            old_name='modified_by',
            new_name='modifiedBy',
        ),
        migrations.RenameField(
            model_name='dictionaryvalues',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='dictionaryvalues',
            old_name='created_by',
            new_name='createdBy',
        ),
        migrations.RenameField(
            model_name='dictionaryvalues',
            old_name='modified_at',
            new_name='modifiedAt',
        ),
        migrations.RenameField(
            model_name='dictionaryvalues',
            old_name='modified_by',
            new_name='modifiedBy',
        ),
        migrations.RenameField(
            model_name='entryfieldspecification',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='entryfieldspecification',
            old_name='created_by',
            new_name='createdBy',
        ),
        migrations.RenameField(
            model_name='entryfieldspecification',
            old_name='default_value',
            new_name='defaultValue',
        ),
        migrations.RenameField(
            model_name='entryfieldspecification',
            old_name='modified_at',
            new_name='modifiedAt',
        ),
        migrations.RenameField(
            model_name='entryfieldspecification',
            old_name='modified_by',
            new_name='modifiedBy',
        ),
        migrations.AlterField(
            model_name='dictionaryvalues',
            name='type',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entryfieldspecification',
            name='ReferencedDict',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='referencing_fields', to='slowniki.dictionary'),
        ),
        migrations.AlterField(
            model_name='entryfieldspecification',
            name='order',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entryfieldspecification',
            name='type',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='entryfieldspecification',
            name='uniqueGroupNumber',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]
