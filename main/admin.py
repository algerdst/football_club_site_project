from django.contrib import admin
from .models import Coach, News, Sign_for_class, About_School, Trains, Student, Gallery, Schedule


@admin.register(Coach)
class AdminCoach(admin.ModelAdmin):
    pass


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    pass


@admin.register(Sign_for_class)
class AdminSign(admin.ModelAdmin):
    pass


@admin.register(About_School)
class AdminAbout_School(admin.ModelAdmin):
    pass


@admin.register(Trains)
class AdminTrains(admin.ModelAdmin):
    pass


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    pass

