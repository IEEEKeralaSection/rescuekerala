# Generated by Django 2.1 on 2018-08-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0088_merge_20180824_1631"),
    ]

    operations = [
        migrations.AddField(
            model_name="ngo",
            name="website_url",
            field=models.CharField(
                default="", max_length=300, verbose_name="Enter your website link"
            ),
        ),
    ]
