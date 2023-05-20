# Generated by Django 4.1.5 on 2023-05-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("M", "Mobile"),
                    ("L", "Laptop"),
                    ("TW", "Top Wear"),
                    ("BW", "Bottom Wear"),
                ],
                max_length=2,
            ),
        ),
    ]
