# Generated by Django 3.2.3 on 2021-06-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_sub_products_sub_productsforher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_productsforher',
            name='price',
            field=models.IntegerField(),
        ),
    ]