# Generated by Django 3.1.7 on 2021-03-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210330_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseinfo',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/course_info', verbose_name='фотоязыкапрограммирования'),
        ),
    ]
