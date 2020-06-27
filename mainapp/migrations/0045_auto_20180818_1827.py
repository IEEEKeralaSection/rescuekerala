# Generated by Django 2.1 on 2018-08-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0044_merge_20180818_1448"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="announcements",
            options={"verbose_name": "Announcement: News", "verbose_name_plural": "Announcements: News",},
        ),
        migrations.AlterModelOptions(
            name="contributor",
            options={"verbose_name": "Contributor: Donation", "verbose_name_plural": "Contributors: Donations",},
        ),
        migrations.AlterModelOptions(
            name="districtcollection",
            options={"verbose_name": "District: Collection", "verbose_name_plural": "District: Collections",},
        ),
        migrations.AlterModelOptions(
            name="districtmanager",
            options={"verbose_name": "District: Manager", "verbose_name_plural": "District: Managers",},
        ),
        migrations.AlterModelOptions(
            name="districtneed", options={"verbose_name": "District: Need", "verbose_name_plural": "District: Needs",},
        ),
        migrations.AlterModelOptions(
            name="ngo", options={"verbose_name": "Volunteer: NGO", "verbose_name_plural": "Volunteers: NGOs",},
        ),
        migrations.AlterModelOptions(
            name="person", options={"verbose_name": "Relief: Refugee", "verbose_name_plural": "Relief: Refugees",},
        ),
        migrations.AlterModelOptions(
            name="request",
            options={
                "verbose_name": "Relief: Supply Requiement",
                "verbose_name_plural": "Relief: Supply Requirements",
            },
        ),
        migrations.AlterModelOptions(
            name="rescuecamp", options={"verbose_name": "Relief: Camp", "verbose_name_plural": "Relief: Camps",},
        ),
        migrations.AlterModelOptions(
            name="volunteer",
            options={"verbose_name": "Volunteer: Individual", "verbose_name_plural": "Volunteers: Individuals",},
        ),
    ]
