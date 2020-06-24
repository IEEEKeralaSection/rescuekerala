# Generated by Django 2.1 on 2018-08-19 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0059_merge_20180819_2150"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contributor",
            name="phone",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
                verbose_name="Phone - ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
        migrations.AlterField(
            model_name="request",
            name="requestee_phone",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
                verbose_name="Requestee Phone - അപേക്ഷകന്\u200dറെ ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="phone",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10 digit mobile number or landline as 0<std code><phone number>",
                        regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                    )
                ],
                verbose_name="Phone - ഫോണ്\u200d നമ്പര്\u200d",
            ),
        ),
    ]
