# Generated by Django 2.1 on 2018-08-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0033_auto_20180817_1003"),
    ]

    operations = [
        migrations.AddField(
            model_name="rescuecamp",
            name="latlng",
            field=models.CharField(
                blank=True,
                help_text="Comma separated latlng field. Leave blank if you don't know it",
                max_length=100,
                verbose_name="GPS Coordinates",
            ),
        ),
        migrations.AddField(
            model_name="rescuecamp",
            name="map_link",
            field=models.CharField(
                blank=True,
                help_text="Copy and paste the full Google Maps link",
                max_length=250,
                null=True,
                verbose_name="Map link",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="address",
            field=models.TextField(
                blank=True, max_length=150, null=True, verbose_name="Address - വിലാസം"
            ),
        ),
    ]
