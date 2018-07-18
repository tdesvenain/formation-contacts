from django.contrib import admin

# Register your models here.
from exams.models import Exam, Note


class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'date_time', 'get_year')

    def get_year(self, obj):
        return obj.date_time.year
    get_year.short_description = 'year'

admin.site.register(Exam, ExamAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'note')

admin.site.register(Note, NoteAdmin)
