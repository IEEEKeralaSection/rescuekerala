# Generated by Django 2.1 on 2018-08-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0061_auto_20180820_1010"),
    ]

    operations = [
        migrations.AddField(
            model_name="volunteer",
            name="has_consented",
            field=models.BooleanField(default=False),
        ),
    ]
