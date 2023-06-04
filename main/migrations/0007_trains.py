# Generated by Django 4.1.7 on 2023-05-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_about_school_options_alter_about_school_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trains",
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
                        max_length=50, null=True, verbose_name="Название тренировки"
                    ),
                ),
                (
                    "price",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Цена тренировки"
                    ),
                ),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Описание тренировки"),
                ),
            ],
            options={
                "verbose_name": "Тренировки",
                "verbose_name_plural": "Тренировка",
            },
        ),
    ]