# Generated by Django 2.1 on 2018-08-11 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="dateadded",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
