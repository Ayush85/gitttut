# Generated by Django 4.1.4 on 2022-12-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("author", models.CharField(max_length=100)),
                ("email", models.EmailField(default="admin@gmail.com", max_length=254)),
            ],
        ),
    ]
