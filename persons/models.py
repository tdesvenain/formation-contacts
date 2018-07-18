from enum import Enum

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Gender(Enum):
    M = 'm'
    F = 'f'


class PersonTypes(Enum):
    STUDENT = 'b'
    STAFF = 'a'


class PersonManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().defer('student_id')

    def get_displayed(self):
        return self.get_queryset().filter(displayed=True)


class DisplayedPersonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            displayed=True
        )


class Person(models.Model):
    GENDERS_CHOICES = [
        (Gender.M.value, 'Homme'),
        (Gender.F.value, 'Femme'),
    ]
    PERSON_TYPE_CHOICES = [
        (PersonTypes.STAFF.value, _('Staff')),
        (PersonTypes.STUDENT.value, _('Student')),
    ]

    person_type = models.CharField(
        max_length=1,
        choices=PERSON_TYPE_CHOICES,
        db_index=True,
        blank=True,
        null=True,
    )
    global_id = models.CharField(
        verbose_name=_('global id'),
        max_length=10,
        unique=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    function = models.OneToOneField(
        on_delete=models.PROTECT,
        to='functions.Function',
        null=True,
        blank=True,
    )
    student_id = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
    )
    displayed = models.BooleanField(default=True)

    class Meta:
        ordering = ('last_name',)

    objects = PersonManager()
    displayed_objects = DisplayedPersonManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('person-detail')


class StudentManager(models.Manager):

    def get_queryset(self):
        return (
            super()
                .get_queryset()
                .filter(person_type=PersonTypes.STUDENT.value)
        )

    def create(self, **kwargs):
        kwargs.update({
            'person_type': PersonTypes.STUDENT.value,
        })
        return super().create(**kwargs)


class Student(Person):
    objects = StudentManager()

    class Meta:
        proxy = True


class Address(models.Model):
    city = models.CharField('city', max_length=50)
    zipcode = models.CharField('zipcode', max_length=50)
    address = models.CharField('address', max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.address}, {self.zipcode} {self.city}"
