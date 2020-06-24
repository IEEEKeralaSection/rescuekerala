# Generated by Django 2.1 on 2018-08-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0019_districtcollection"),
    ]

    operations = [
        migrations.AddField(
            model_name="volunteer",
            name="is_dm",
            field=models.BooleanField(
                default=False, verbose_name="Is district manager"
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="is_spoc",
            field=models.BooleanField(
                default=False, verbose_name="Is point of contact"
            ),
        ),
    ]
