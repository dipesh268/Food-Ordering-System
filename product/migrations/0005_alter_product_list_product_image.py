# Generated by Django 5.0.7 on 2024-08-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_t_alter_product_list_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_list',
            name='product_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
