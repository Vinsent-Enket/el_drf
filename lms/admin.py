from django.contrib import admin

from lms.models import Lesson, Course


# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )

