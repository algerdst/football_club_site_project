# Generated by Django 4.1.7 on 2023-06-11 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                        max_length=50,
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
            options={
                "verbose_name": "Абзац с описанием школы",
                "verbose_name_plural": "Абзацы с описанием школы",
            },
        ),
        migrations.CreateModel(
            name="Coach",
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
                    "name",
                    models.CharField(max_length=50, null=True, verbose_name="Ф.И.О"),
                ),
                (
                    "photo",
                    models.ImageField(
                        default="default_coach",
                        upload_to="coach_pics",
                        verbose_name="Фото",
                    ),
                ),
                ("description", models.TextField(null=True, verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Тренер",
                "verbose_name_plural": "Тренерский состав",
            },
        ),
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery")),
            ],
            options={
                "verbose_name": "Картинка для галереи",
                "verbose_name_plural": "Галерея",
            },
        ),
        migrations.CreateModel(
            name="Sign_for_class",
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
                    "name",
                    models.CharField(max_length=50, null=True, verbose_name="Имя"),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="Почта"),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=1000, null=True, verbose_name="Комментарий"
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка на занятие",
                "verbose_name_plural": "Заявки на занятия",
            },
        ),
        migrations.CreateModel(
            name="Student",
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
                    "name",
                    models.CharField(max_length=50, null=True, verbose_name="Ф.И.О"),
                ),
                (
                    "photo",
                    models.ImageField(
                        default="default_student",
                        upload_to="student_pics",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Описание результатов"),
                ),
            ],
            options={
                "verbose_name": "Ученик",
                "verbose_name_plural": "Ученики",
            },
        ),
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
                (
                    "age",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Возраст ребенка"
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        max_length=50,
                        null=True,
                        verbose_name="Продолжительность тренировки",
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        max_length=50,
                        null=True,
                        verbose_name="Периодичность тренировок",
                    ),
                ),
                (
                    "cost_of_first_train",
                    models.CharField(
                        default="Первая тренировка: бесплатно!",
                        max_length=50,
                        verbose_name="Стоймость первой тренировки",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to="trains_pics", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тренировка",
                "verbose_name_plural": "Тренировки",
            },
        ),
        migrations.CreateModel(
            name="Schedule",
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
                ("group_ages", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                ("days", models.CharField(max_length=20)),
                (
                    "coach_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.coach"
                    ),
                ),
            ],
            options={
                "verbose_name": "Расписание",
                "verbose_name_plural": "Расписание занятий",
            },
        ),
    ]
