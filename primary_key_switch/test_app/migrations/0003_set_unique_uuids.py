# Generated by Django 4.0.6 on 2022-07-18 09:40

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    TestModel = apps.get_model('test_app', 'TestModel')

    for instance in TestModel.objects.all():
        instance.uuid = uuid.uuid4()
        instance.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_testmodel_uuid'),
    ]

    operations = [migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop)]
