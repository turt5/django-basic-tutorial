# Generated by Django 5.0.6 on 2024-05-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=7)),
                ('courseName', models.CharField(max_length=100)),
            ],
        ),
    ]
