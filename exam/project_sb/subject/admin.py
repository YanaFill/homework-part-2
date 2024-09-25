from django.contrib import admin
from .models import Subject, LessonType

admin.site.register(LessonType)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'lesson_type', 'control', 'specialty', 'semester')
    search_fields = ('name', 'teacher', 'specialty')
    list_filter = ('lesson_type', 'control', 'semester')
    ordering = ('name',)
