# Generated by Django 2.1 on 2018-08-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0067_auto_20180821_1637"),
    ]

    operations = [
        migrations.RemoveField(model_name="privaterescuecamp", name="taluk",),
        migrations.RemoveField(model_name="privaterescuecamp", name="village",),
        migrations.AddField(
            model_name="privaterescuecamp",
            name="city",
            field=models.CharField(
                default="", max_length=150, verbose_name="City - നഗരം"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="privaterescuecamp",
            name="is_inside_kerala",
            field=models.BooleanField(
                default=False,
                verbose_name="Center inside kerala? - കേന്ദ്രം കേരളത്തിലാണോ",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="privaterescuecamp",
            name="lsg_name",
            field=models.CharField(
                blank=True,
                max_length=150,
                null=True,
                verbose_name="LSG Name - സ്വയംഭരണ സ്ഥാപനത്തിന്റെ പേര്",
            ),
        ),
        migrations.AddField(
            model_name="privaterescuecamp",
            name="lsg_type",
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (0, "Corporation"),
                    (1, "Municipality"),
                    (2, "Grama Panchayath"),
                ],
                null=True,
                verbose_name="LSG Type - തദ്ദേശ സ്വയംഭരണ സ്ഥാപനം",
            ),
        ),
        migrations.AddField(
            model_name="privaterescuecamp",
            name="ward_name",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="Ward - വാർഡ്"
            ),
        ),
    ]
