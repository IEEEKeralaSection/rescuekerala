# Generated by Django 2.1 on 2018-08-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0070_merge_20180821_2307"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="checkin_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Check-in Date - ചെക്ക്-ഇൻ തീയതി"
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="checkout_date",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Check-out Date - ചെക്ക്-ഔട്ട് തീയതി",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("new", "New"),
                    ("checked_out", "Checked Out"),
                    ("closed", "Closed"),
                ],
                default=None,
                max_length=15,
                null=True,
            ),
        ),
    ]
