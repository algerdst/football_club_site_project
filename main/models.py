from django.db import models


class Coach(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Ф.И.О')
    photo = models.ImageField(upload_to='coach_pics', default='default_coach', verbose_name='Фото')
    description = models.TextField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренерский состав'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Ф.И.О')
    photo = models.ImageField(upload_to='student_pics', default='default_student', verbose_name='Фото')
    description = models.TextField(null=True, verbose_name='Описание результатов')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Название')
    image = models.ImageField(upload_to='news_pics', default='default_new', verbose_name='Изображение')
    description = models.TextField(max_length=5000, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости клуба'

    def __str__(self):
        return self.title


# Модель заявки для записи на занятие
class Sign_for_class(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    phone = models.CharField(null=True, verbose_name='Номер телефона',blank=True, max_length=20)
    email = models.EmailField(null=True, verbose_name='Почта')
    description = models.TextField(max_length=1000, null=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявка на занятие'
        verbose_name_plural = 'Заявки на занятия'

    def __str__(self):
        return self.phone


class About_School(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Название абзаца о футбольной школе')
    text = models.TextField(null=True, verbose_name='Описание абзаца о футбольной школе')
    image = models.ImageField(upload_to='site_images', verbose_name='Картинка к абзацу о футбольной школе')

    class Meta:
        verbose_name = 'Абзац с описанием школы'
        verbose_name_plural = 'Абзацы с описанием школы'

    def __str__(self):
        return self.title


class Trains(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='Название тренировки')
    price = models.CharField(max_length=50, null=True, verbose_name='Цена тренировки')
    description = models.TextField(null=True, verbose_name='Описание тренировки')
    age = models.CharField(max_length=50, null=True, verbose_name='Возраст ребенка')
    duration = models.CharField(max_length=50, null=True, verbose_name='Продолжительность тренировки')
    frequency = models.CharField(max_length=50, null=True, verbose_name='Периодичность тренировок')
    cost_of_first_train = models.CharField(max_length=50, default='Первая тренировка: бесплатно!',
                                           verbose_name='Стоймость первой тренировки')
    image=models.ImageField(upload_to='trains_pics',verbose_name='Изображение', null=True)

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery')

    class Meta:
        verbose_name = 'Картинка для галереи'
        verbose_name_plural = 'Галерея'


class Schedule(models.Model):
    coach_name=models.ForeignKey(Coach, on_delete=models.CASCADE)
    group_ages=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    days=models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание занятий'

    def __str__(self):
        return f'Расписание занятий тренера {self.coach_name}'