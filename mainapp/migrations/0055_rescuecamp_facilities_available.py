# Generated by Django 2.1 on 2018-08-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0054_auto_20180819_1211"),
    ]

    operations = [
        migrations.AddField(
            model_name="rescuecamp",
            name="facilities_available",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Facilities existing, (light, kitchen, toilets), etc - ലഭ്യമായ സൗകര്യങ്ങൾ ",
            ),
        ),
    ]
