# Generated by Django 2.1 on 2018-09-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0092_auto_20180828_1407"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person", name="name", field=models.CharField(max_length=51, verbose_name="Name - പേര്"),
        ),
    ]
