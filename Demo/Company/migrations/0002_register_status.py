# Generated by Django 4.2.11 on 2024-04-03 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
