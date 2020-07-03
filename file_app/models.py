from django.db import models

from common.validators import validate_file_extension


class FileTypeChoices(models.TextChoices):
    BRAND_LOGO = 1, 'Логотип бренда'
    CATEGORY_ICON = 2, 'Иконка категории'
    PRODUCT_IMAGE = 3, 'Изображение товара'


class File(models.Model):

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    file = models.FileField(
        'Файл',
        upload_to='upload/',
        validators=[validate_file_extension]
    )
    type = models.IntegerField(
        'Тип файла',
        choices=FileTypeChoices.choices
    )
    product = models.ForeignKey(
        'market.Product',
        verbose_name='Товар',
        related_name='files',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        'Доступен к просмотру',
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.file.name

    def __str__(self):
        return self.__unicode__()
