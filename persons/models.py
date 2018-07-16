from enum import Enum

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Gender(Enum):
    M = 'm'
    F = 'f'


class Person(models.Model):
    GENDERS_CHOICES = [
        (Gender.M.value, 'Homme'),
        (Gender.F.value, 'Femme'),
    ]

    global_id = models.CharField(
        verbose_name=_('global id'),
        max_length=10,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    function = models.ForeignKey(
        on_delete=models.PROTECT,
        to='functions.Function',
        null=True,
        blank=True,
    )
    displayed = models.BooleanField(default=True)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # # python < 3.6
        # return "{} {}".format(
        #    self.first_name,
        #    self.last_name,
        # )

    def get_absolute_url(self):
        return reverse('person-detail')


class Address(models.Model):
    city = models.CharField('city', max_length=50)
    zipcode = models.CharField('zipcode', max_length=50)
    address = models.CharField('address', max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return  f"{self.address}, {self.zipcode} {self.city}"
