# Generated by Django 4.1.7 on 2023-05-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_alter_trains_options_trains_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="trains",
            name="image",
            field=models.ImageField(
                null=True, upload_to="trains_pics", verbose_name="Изображение"
            ),
        ),
    ]
