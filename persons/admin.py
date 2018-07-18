from django.contrib import admin

# Register your models here.
from persons.models import Person, Address, Student


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'birth_date',
        'gender',
        'global_id',
        'function',
        'person_type',
    )
    search_fields = (
        'first_name',
        'last_name',
        'global_id',
    )
    list_filter = (
        'gender',
    )
    ordering = ('-birth_date',)
    autocomplete_fields = ('function',)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'birth_date',
        'gender',
        'student_id',
    )
    search_fields = (
        'first_name',
        'last_name',
        'student_id',
    )
    list_filter = (
        'gender',
    )
    ordering = ('-birth_date',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Address)
