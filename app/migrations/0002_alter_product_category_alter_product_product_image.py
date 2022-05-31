# Generated by Django 4.0.4 on 2022-05-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B', 'BAGS'), ('J', 'JACKET'), ('CL', 'CLAY UTENSIL'), ('D', 'DUFFLES')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]