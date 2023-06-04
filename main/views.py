from django.shortcuts import render
from .models import About_School, Trains, Coach, Student, Gallery, Sign_for_class, Schedule
from .forms import SignForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data['name'],
                f'''{form.cleaned_data['email']},
                         {form.cleaned_data['phone']},
                         {form.cleaned_data['description']}
                    ''',
                settings.EMAIL_HOST_USER,
                ['stadolnikoff@yandex.ru'],
                fail_silently=False,
            )
            messages.success(request, 'Ваша заявка успешно отправлена')
    else:
        form = SignForm()
    data = {
        'paragraphs': About_School.objects.all(),
        'trains': Trains.objects.all(),
        'form': form,
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data['name'],
                f'''{form.cleaned_data['email']},
                                     {form.cleaned_data['phone']},
                                     {form.cleaned_data['description']}
                                ''',
                settings.EMAIL_HOST_USER,
                ['stadolnikoff@yandex.ru'],
                fail_silently=False,
            )
            messages.success(request, 'Ваша заявка успешно отправлена')
    else:
        form = SignForm()
    data = {
        'form': form,
        'coaches': Coach.objects.all(),
        'students': Student.objects.all(),
        'pictures': Gallery.objects.all(),
        'picture': Gallery.objects.last(),

    }
    return render(request, 'main/about_school.html', context=data)


def trains(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data['name'],
                f'''{form.cleaned_data['email']},
                                     {form.cleaned_data['phone']},
                                     {form.cleaned_data['description']}
                                ''',
                settings.EMAIL_HOST_USER,
                ['stadolnikoff@yandex.ru'],
                fail_silently=False,
            )
            messages.success(request, 'Ваша заявка успешно отправлена')
    else:
        form = SignForm()
    data = {
        'schedules':Schedule.objects.all(),
        'trains':Trains.objects.all(),
        'form': form
    }
    return render(request, 'main/trains.html', context=data)


def contacts(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data['name'],
                f'''{form.cleaned_data['email']},
                                     {form.cleaned_data['phone']},
                                     {form.cleaned_data['description']}
                                ''',
                settings.EMAIL_HOST_USER,
                ['stadolnikoff@yandex.ru'],
                fail_silently=False,
            )
            messages.success(request, 'Ваша заявка успешно отправлена')
    else:
        form = SignForm()
    data = {
        'form': form
    }
    return render(request, 'main/contacts.html', context=data)
