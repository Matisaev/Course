# Generated by Django 3.1.7 on 2021-03-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20210331_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Описание курса'),
        ),
    ]
