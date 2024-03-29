# Generated by Django 4.0.6 on 2022-07-18 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Test Model',
            },
        ),
        migrations.CreateModel(
            name='TestManyToManyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_models', models.ManyToManyField(related_name='test_manytomany_models', to='test_app.testmodel')),
            ],
            options={
                'verbose_name': 'Test ManyToMany Model',
            },
        ),
        migrations.CreateModel(
            name='TestForeignKeyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodel')),
            ],
            options={
                'verbose_name': 'Test ForeignKey Model',
            },
        ),
    ]
