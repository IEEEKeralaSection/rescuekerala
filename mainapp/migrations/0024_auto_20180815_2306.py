# Generated by Django 2.1 on 2018-08-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0023_auto_20180815_1848"),
    ]

    operations = [
        migrations.AlterField(model_name="districtmanager", name="phone", field=models.CharField(max_length=11),),
    ]
