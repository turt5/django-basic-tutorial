# Generated by Django 5.0.6 on 2024-05-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseCode',
            field=models.CharField(max_length=10),
        ),
    ]