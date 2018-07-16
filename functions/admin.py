from django.contrib import admin

# Register your models here.
from functions.models import Function

class FunctionAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Function, FunctionAdmin)
