# Generated by Django 4.0.5 on 2022-06-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_catagory_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(choices=[('mobile', 'MOBILE'), ('lipstick', 'LIPStick'), ('baal', 'BAAL')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
