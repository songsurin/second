# Generated by Django 4.2 on 2023-04-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "userid",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("passwd", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=20, null=True)),
                ("tel", models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
