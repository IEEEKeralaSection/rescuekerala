# Generated by Django 2.1 on 2018-08-18 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0046_rescuecamp_total_people"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contributor",
            name="phone",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile", message="Please Enter 10 digit mobile number", regex="^[6-9]\\d{9}$",
                    )
                ],
                verbose_name="Phone - ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="district",
            field=models.CharField(
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
                verbose_name="District - ജില്ല",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="requestee_phone",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile", message="Please Enter 10 digit mobile number", regex="^[6-9]\\d{9}$",
                    )
                ],
                verbose_name="Requestee Phone - അപേക്ഷകന്\u200dറെ ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="phone",
            field=models.CharField(
                max_length=10,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile", message="Please Enter 10 digit mobile number", regex="^[6-9]\\d{9}$",
                    )
                ],
                verbose_name="Phone - ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
    ]
