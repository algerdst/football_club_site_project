# Generated by Django 4.1.7 on 2023-06-01 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_alter_sign_for_class_phone_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sign_for_class",
            old_name="phone_number",
            new_name="phone",
        ),
    ]
