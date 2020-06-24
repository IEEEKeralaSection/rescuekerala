# Generated by Django 2.1 on 2018-08-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0029_merge_20180816_2112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contributor",
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
            ),
        ),
        migrations.AlterField(
            model_name="districtcollection",
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
            ),
        ),
        migrations.AlterField(
            model_name="districtmanager",
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
            ),
        ),
        migrations.AlterField(
            model_name="districtneed",
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
                verbose_name="Districts - ജില്ല",
            ),
        ),
        migrations.AlterField(
            model_name="rescuecampdetails",
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
            ),
        ),
        migrations.AlterField(
            model_name="volunteer",
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
            ),
        ),
    ]
