# Generated by Django 4.2 on 2023-05-08 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_code", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
                ("description", models.TextField()),
                (
                    "filename",
                    models.CharField(blank=True, default="", max_length=500, null=True),
                ),
            ],
        ),
    ]
