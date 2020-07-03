from django.db import models

from common.validators import validate_file_extension


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )
    name = models.CharField(
        'Наименование',
        max_length=100
    )
    icon = models.ForeignKey(
        'file_app.File',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    index = models.IntegerField(
        'Порядковый номер',
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Brand(models.Model):
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField(
        verbose_name='Наименование',
        max_length=100
    )
    logo = models.ForeignKey(
        'file_app.File',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    detail = models.CharField(
        'Описание',
        max_length=2000,
        null=True,
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

