from django.contrib import admin

# Register your models here.
from persons.models import Person, Address


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'birth_date',
        'gender',
        'global_id',
        'function',
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


admin.site.register(Person, PersonAdmin)
admin.site.register(Address)
