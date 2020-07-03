# Generated by Django 3.0.8 on 2020-07-03 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dicts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Группа свойств',
                'verbose_name_plural': 'Группы свойств',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('detail', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('is_filter', models.BooleanField(default=False, verbose_name='Фильтр поиска')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='market.GroupProperties', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Свойство',
                'verbose_name_plural': 'Свойства',
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000, verbose_name='Значение')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='market.Property', verbose_name='Свойство')),
            ],
            options={
                'verbose_name': 'Характеристика товара',
                'verbose_name_plural': 'Характеристики товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Цена')),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Закупочная стоимость')),
                ('on_sale', models.BooleanField(default=False, verbose_name='В продаже')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='Рекомендованный')),
                ('is_popular', models.BooleanField(default=False, verbose_name='Популярный')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новинка')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='dicts.Brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='dicts.Category', verbose_name='Категория товара')),
                ('characteristics', models.ManyToManyField(related_name='products', to='market.ProductCharacteristics', verbose_name='Характеристики')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]