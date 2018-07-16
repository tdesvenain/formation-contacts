from django.forms import inlineformset_factory, ModelForm

from persons.models import Person, Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


AddressFormSet = inlineformset_factory(
    Person,
    Address,
    form=AddressForm,
    max_num=3,
    extra=1,
)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'global_id',
        ]
