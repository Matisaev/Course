# Generated by Django 3.1.7 on 2021-03-31 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20210331_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesignup',
            name='courseinfo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_signup', to='course.courseinfo', verbose_name='Информация о курсах'),
        ),
    ]