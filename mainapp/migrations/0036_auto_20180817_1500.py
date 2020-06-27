# Generated by Django 2.1 on 2018-08-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0035_auto_20180817_1339"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngo",
            name="organisation_address",
            field=models.TextField(default="", verbose_name="Address of Organization"),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="organisation",
            field=models.CharField(max_length=250, verbose_name="Name of Organization (സംഘടനയുടെ പേര്)"),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="organisation_type",
            field=models.CharField(max_length=250, verbose_name="Type of Organization"),
        ),
    ]
