# Generated by Django 3.1.7 on 2021-03-29 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210329_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseinfo',
            old_name='courses_id',
            new_name='course_id',
        ),
    ]