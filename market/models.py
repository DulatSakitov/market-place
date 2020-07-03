from django.db import models


class GroupProperties(models.Model):

    class Meta:
        verbose_name = 'Группа свойств'
        verbose_name_plural = 'Группы свойств'

    name = models.CharField(
        verbose_name='Наименование',
        max_length=200
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Property(models.Model):

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'

    name = models.CharField(
        verbose_name='Наименование',
        max_length=200
    )
    detail = models.CharField(
        verbose_name='Описание',
        max_length=2000,
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        'market.GroupProperties',
        verbose_name='Группа',
        related_name='properties',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_filter = models.BooleanField(
        verbose_name='Фильтр поиска',
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class ProductCharacteristics(models.Model):

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'

    property = models.ForeignKey(
        'market.Property',
        verbose_name='Свойство',
        related_name='values',
        on_delete=models.CASCADE
    )
    value = models.CharField(
        verbose_name='Значение',
        max_length=1000
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %s" % (self.property.name, self.value)

    def __str__(self):
        return self.__unicode__()


class Product(models.Model):

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField(
        'Наименование',
        max_length=200
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=19,
        decimal_places=2
    )
    purchase_price = models.DecimalField(
        verbose_name='Закупочная стоимость',
        max_digits=19,
        decimal_places=2,
        null=True,
        blank=True
    )
    on_sale = models.BooleanField(
        verbose_name='В продаже',
        default=False
    )
    category = models.ForeignKey(
        'dicts.Category',
        related_name='products',
        verbose_name='Категория товара',
        on_delete=models.SET_NULL,
        null=True
    )
    brand = models.ForeignKey(
        'dicts.Brand',
        related_name='products',
        verbose_name='Бренд',
        on_delete=models.SET_NULL,
        null=True
    )
    characteristics = models.ManyToManyField(
        'market.ProductCharacteristics',
        verbose_name='Характеристики',
        related_name='products'
    )
    is_recommended = models.BooleanField(
        verbose_name='Рекомендованный',
        default=False
    )
    is_popular = models.BooleanField(
        verbose_name='Популярный',
        default=False
    )
    is_new = models.BooleanField(
        verbose_name='Новинка',
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()
