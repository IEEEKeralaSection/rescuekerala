# Generated by Django 2.1 on 2018-08-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0074_auto_20180822_0537"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="unique_identifier",
            field=models.CharField(default="", max_length=32),
        ),
    ]
