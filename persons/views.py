# Create your views here.

from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.base import View

# def welcome(request: HttpRequest) -> HttpResponse:
#    return HttpResponse('<h1>Bienvenue sur la gestion des personnes</h1>')
from persons.models import Person


class Welcome(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Bienvenue sur la gestion des personnes (class based)</h1>')


class PersonList(ListView):
    model = Person

    # paginate_by = 1

    def get_queryset(self):
        return super().get_queryset().filter(displayed=True)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['now'] = now()
        return context_data


class PersonDetail(DetailView):
    model = Person
    slug_field = 'global_id'


class PersonUpdate(UpdateView):
    model = Person
    slug_field = 'global_id'
    fields = [
        'first_name',
        'last_name',
        'birth_date',
    ]


class PersonDelete(DeleteView):
    model = Person
    slug_field = 'global_id'

    def get_success_url(self):
        return reverse('person-list')


class PersonCreate(CreateView):
    model = Person
    fields = [
        'first_name',
        'last_name',
        'birth_date',
        'global_id',
    ]
    #
    # def get_success_url(self):
    #     super().get_success_url()
    #     return reverse(
    #         'person-detail',
    #         kwargs={'slug': self.object.global_id}
    #     )
