# Generated by Django 4.2 on 2023-04-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
