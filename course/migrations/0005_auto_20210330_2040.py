# Generated by Django 3.1.7 on 2021-03-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20210330_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='image',
            field=models.ImageField(upload_to='media/course_info', verbose_name='фотоязыкапрограммирования'),
        ),
    ]
