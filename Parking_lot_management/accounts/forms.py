from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Customer

class BasicForm(forms.Form):
    def disable_field(self, field):
        """
        marks field as disabled
        :param field:
        :return:
        """
        self.fields[field].widget.attrs['disabled'] = ""

    def mark_error(self, field, description):
        """
        Marks the given field as errous. The given description is displayed when the form it generated
        :param field: name of the field
        :param description: The error description
        :return:
        """
        self._errors[field] = self.error_class([description])
        del self.cleaned_data[field]

    def clear_errors(self):
        self._errors = {}


def setup_field(field, placeholder=None):
    """
    This configures the given field to play nice with the bootstrap theme. Additionally, you can add
    an additional argument to set a placeholder text on the field.
    :param field:
    :param placeholder:
    :return:
    """
    field.widget.attrs['class'] = 'form-control'
    if placeholder is not None:
        field.widget.attrs['placeholder'] = placeholder


class CustomerForm(BasicForm):
    firstname = forms.CharField(label='First Name', max_length=50)
    setup_field(firstname, 'Enter first name here')
    lastname = forms.CharField(label='Last Name', max_length=50)
    setup_field(lastname, 'Enter last name here')
    sex = forms.ChoiceField(required=False, choices=Customer.GENDER)
    setup_field(sex)
    phone = forms.CharField(required=False, max_length=10)
    setup_field(phone, 'Enter phone number here')

    def assign(self, profile):
        profile.firstname = self.cleaned_data['firstname']
        profile.lastname = self.cleaned_data['lastname']
        profile.sex = self.cleaned_data['sex']
        profile.phone = self.cleaned_data['phone']
