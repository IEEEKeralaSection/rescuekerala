# Generated by Django 2.1 on 2018-08-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0063_auto_20180821_0820"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requestupdate",
            name="other_status",
            field=models.CharField(
                blank=True,
                default="",
                max_length=255,
                verbose_name="Please specify other status",
            ),
        ),
    ]
