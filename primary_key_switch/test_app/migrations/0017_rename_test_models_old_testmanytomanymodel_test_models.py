# Generated by Django 4.0.6 on 2022-07-18 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0016_remove_testmanytomanymodel_test_models_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testmanytomanymodel',
            old_name='test_models_old',
            new_name='test_models',
        ),
    ]
