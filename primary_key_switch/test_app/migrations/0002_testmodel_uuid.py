# Generated by Django 4.0.6 on 2022-07-18 09:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]