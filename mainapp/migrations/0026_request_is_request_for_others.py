# Generated by Django 2.1 on 2018-08-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0025_auto_20180816_1203"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="is_request_for_others",
            field=models.BooleanField(
                default=False,
                verbose_name="Requesting for others - മറ്റൊരാൾക്ക് വേണ്ടി അപേക്ഷിക്കുന്നു  ",
            ),
        ),
    ]
