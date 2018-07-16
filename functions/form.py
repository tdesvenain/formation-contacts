from django.forms import ModelForm

from functions.models import Function


class FunctionForm(ModelForm):

    class Meta:
        model = Function
        fields = ['title']
