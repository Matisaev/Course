# Generated by Django 3.1.7 on 2021-03-31 13:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20210331_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesignup',
            name='programming_languages_id',
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=35, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=35, message='Не более 20 символов'), django.core.validators.MinLengthValidator(limit_value=3, message='не менее 3 символов')]),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='address',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/course_info', verbose_name='фотоязыкапрограммирования'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='title',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Название курса'),
        ),
        migrations.AlterField(
            model_name='coursesignup',
            name='courseinfo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_signup', to='course.courseinfo', verbose_name='Информация о курсах'),
        ),
        migrations.AlterField(
            model_name='programminglanguages',
            name='title',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=100, message='Не более 30 символов'), django.core.validators.MinLengthValidator(limit_value=2, message='не менее 2 символов')]),
        ),
    ]
