# Generated by Django 2.1 on 2018-08-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0033_auto_20180817_1003"),
    ]

    operations = [
        migrations.CreateModel(
            name="NGO",
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
                            ("alp", "Alappuzha - ആലപ്പുഴ"),
                            ("ekm", "Ernakulam - എറണാകുളം"),
                            ("idk", "Idukki - ഇടുക്കി"),
                            ("knr", "Kannur - കണ്ണൂർ"),
                            ("ksr", "Kasaragod - കാസർഗോഡ്"),
                            ("kol", "Kollam - കൊല്ലം"),
                            ("ktm", "Kottayam - കോട്ടയം"),
                            ("koz", "Kozhikode - കോഴിക്കോട്"),
                            ("mpm", "Malappuram - മലപ്പുറം"),
                            ("pkd", "Palakkad - പാലക്കാട്"),
                            ("ptm", "Pathanamthitta - പത്തനംതിട്ട"),
                            ("tvm", "Thiruvananthapuram - തിരുവനന്തപുരം"),
                            ("tcr", "Thrissur - തൃശ്ശൂർ"),
                            ("wnd", "Wayanad - വയനാട്"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "organisation",
                    models.CharField(
                        max_length=250, verbose_name="Name of Organization (സംഘടന)"
                    ),
                ),
                (
                    "organisation_type",
                    models.CharField(
                        max_length=250, verbose_name="Type of Organization (സംഘടന)"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Contact Person"),
                ),
                ("phone", models.CharField(max_length=10)),
                ("description", models.TextField(verbose_name="About Organisation")),
                (
                    "area",
                    models.CharField(
                        max_length=500, verbose_name="Area of volunteering"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        max_length=500, verbose_name="Preferred Location to Volunteer"
                    ),
                ),
                (
                    "is_spoc",
                    models.BooleanField(
                        default=False, verbose_name="Is point of contact"
                    ),
                ),
                ("joined", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
