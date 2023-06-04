# Generated by Django 4.1.7 on 2023-05-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_sign_for_class"),
    ]

    operations = [
        migrations.CreateModel(
            name="About_School",
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
                (
                    "title",
                    models.CharField(
                        max_length=25,
                        null=True,
                        verbose_name="Название абзаца о футбольной школе",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        null=True, verbose_name="Описание абзаца о футбольной школе"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="site_images",
                        verbose_name="Картинка к абзацу о футбольной школе",
                    ),
                ),
            ],
        ),
    ]
