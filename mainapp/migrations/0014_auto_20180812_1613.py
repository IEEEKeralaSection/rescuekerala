# Generated by Django 2.1 on 2018-08-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0013_auto_20180812_1547"),
    ]

    operations = [
        migrations.CreateModel(
            name="DistrictNeeds",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("tvm", "Thiruvananthapuram"),
                            ("ptm", "Pathanamthitta"),
                            ("alp", "Alappuzha"),
                            ("ktm", "Kottayam"),
                            ("idk", "Idukki"),
                            ("mpm", "Malappuram"),
                            ("koz", "Kozhikode"),
                            ("wnd", "Wayanad"),
                            ("knr", "Kannur"),
                            ("ksr", "Kasaragod"),
                            ("pkd", "Palakkad"),
                            ("tcr", "Thrissur"),
                            ("ekm", "Ernakulam"),
                            ("kol", "Kollam"),
                        ],
                        max_length=15,
                    ),
                ),
                ("needs", models.TextField()),
                ("status", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="contributor",
            name="commodities",
            field=models.TextField(
                verbose_name="What you can contribute. Eg: Shirts, torches etc"
            ),
        ),
    ]
