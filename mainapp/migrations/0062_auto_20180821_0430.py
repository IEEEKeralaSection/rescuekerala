# Generated by Django 2.1 on 2018-08-20 23:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0061_auto_20180820_1010"),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestUpdate",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID",),),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("pro", "In progess"),
                            ("res", "Resolved"),
                            ("dup", "Duplicate"),
                            ("cls", "Closed"),
                            ("otr", "Other"),
                            ("sup", "Supplied"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "other_status",
                    models.CharField(
                        default="",
                        max_length=255,
                        verbose_name="Status description if none of the default statuses are applicable",
                    ),
                ),
                ("updater_name", models.CharField(max_length=100, verbose_name="Name of person or group updating"),),
                (
                    "updater_phone",
                    models.CharField(
                        max_length=14,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_mobile",
                                message="Please Enter 10/11 digit mobile number or\
                                 landline as 0<std code><phone number>",
                                regex="^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$",
                            )
                        ],
                        verbose_name="Phone number of person or group updating",
                    ),
                ),
                ("notes", models.TextField(blank=True, verbose_name="Volunteer comments"),),
                ("update_ts", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="request",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("pro", "In progess"),
                    ("res", "Resolved"),
                    ("dup", "Duplicate"),
                    ("cls", "Closed"),
                    ("otr", "Other"),
                    ("sup", "Supplied"),
                ],
                default="new",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="requestupdate",
            name="request",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.Request"),
        ),
    ]
