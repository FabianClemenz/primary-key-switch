# Generated by Django 4.0.6 on 2022-07-18 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0012_rename_test_model_uuid_testforeignkeymodel_test_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testforeignkeymodel',
            name='test_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_model', to='test_app.testmodel'),
        ),
        migrations.AlterField(
            model_name='testmanytomanymodel',
            name='test_models',
            field=models.ManyToManyField(related_name='test_manytomany_models', through='test_app.TestThroughModel', to='test_app.testmodel'),
        ),
        migrations.AlterField(
            model_name='testthroughmodel',
            name='test_many_to_many_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmanytomanymodel'),
        ),
        migrations.AlterField(
            model_name='testthroughmodel',
            name='test_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodel'),
        ),
    ]
