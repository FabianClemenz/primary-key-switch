from django.db import models
import uuid

# Create your models here.


class TestModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200, verbose_name="Name")

    class Meta:
        verbose_name = "Test Model"


class TestForeignKeyModel(models.Model):
    test_model = models.ForeignKey(TestModel, to_field='uuid', on_delete=models.CASCADE, related_name='test_model')

    class Meta:
        verbose_name = "Test ForeignKey Model"


class TestManyToManyModel(models.Model):
    test_models = models.ManyToManyField(TestModel, related_name='test_manytomany_models')

    class Meta:
        verbose_name = "Test ManyToMany Model"
