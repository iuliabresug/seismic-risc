# Generated by Django 2.2.4 on 2019-09-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('map_app', '0003_auto_20190928_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='an_construire',
            field=models.IntegerField(default=-1),
        ),
    ]