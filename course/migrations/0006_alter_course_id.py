# Generated by Django 4.1.2 on 2023-01-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]