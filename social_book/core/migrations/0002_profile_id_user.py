# Generated by Django 4.1.7 on 2023-02-28 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
