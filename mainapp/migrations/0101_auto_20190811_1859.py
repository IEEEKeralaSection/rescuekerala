# Generated by Django 2.1.2 on 2019-08-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0100_auto_20190811_1204"),
    ]

    operations = [
        migrations.AlterModelOptions(name="collectioncenter", options={"verbose_name": "Private collection centers"},),
        migrations.AlterModelOptions(
            name="districtneed",
            options={
                "verbose_name": "District: Need and Collection center",
                "verbose_name_plural": "District: Needs and Collection centers",
            },
        ),
        migrations.AddField(
            model_name="districtneed", name="inventory", field=models.TextField(default=""), preserve_default=False,
        ),
    ]
