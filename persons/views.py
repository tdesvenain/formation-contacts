# Create your views here.
from django.contrib.postgres.aggregates import StringAgg, JSONBAgg
from django.db.models import Prefetch, Count, Max
from django.http import HttpResponse
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.base import View
# def welcome(request: HttpRequest) -> HttpResponse:
#    return HttpResponse('<h1>Bienvenue sur la gestion des personnes</h1>')
from extra_views import UpdateWithInlinesView, InlineFormSet

from persons.models import Person, Address


class Welcome(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Bienvenue sur la gestion des personnes (class based)</h1>')


class PersonList(ListView):
    model = Person

    # paginate_by = 1

    def get_queryset(self):
        return (
            Person.objects.get_displayed()
                .select_related('function')
                .prefetch_related(Prefetch(
                'addresses',
                queryset=Address.objects.only('person_id', 'city')
                    .distinct('person_id')
                    .order_by('person_id', '-pk')
                # to_attr='addresses'
            )).annotate(
                city_agg=StringAgg('addresses__city', ', ', distinct=True),
                addr_count=Count('addresses'),
            )
        )

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['now'] = now()
        return context_data


class PersonDetail(DetailView):
    model = Person
    slug_field = 'global_id'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related('function').defer('displayed')


class AddressesInline(InlineFormSet):
    model = Address
    fields = '__all__'
    factory_kwargs = {'extra': 1}


class PersonUpdate(UpdateWithInlinesView):
    model = Person
    slug_field = 'global_id'
    inlines = [AddressesInline]
    fields = '__all__'

    #
    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     valid = super().form_valid(form)
    #     address_formset = self.get_context_data()['address_formset']
    #     if address_formset.is_valid():
    #         address_formset.save()
    #     return valid
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         address_formset = AddressFormSet(self.request.POST, instance=self.object)
    #     else:
    #         address_formset = AddressFormSet(instance=self.object)
    #     context_data['address_formset'] = address_formset
    #     return context_data
    #
    def get_success_url(self):
        return reverse(
            'person-detail',
            kwargs={'slug': self.object.global_id}
        )


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

    def get_success_url(self):
        # super().get_success_url()
        return reverse(
            'person-detail',
            kwargs={'slug': self.object.global_id}
        )
