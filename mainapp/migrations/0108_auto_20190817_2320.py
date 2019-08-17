# Generated by Django 2.1.2 on 2019-08-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0107_auto_20190817_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsjob',
            name='failure',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='smsjob',
            name='has_completed',
            field=models.BooleanField(default=False),
        ),
    ]