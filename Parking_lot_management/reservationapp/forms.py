from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class DurationForm(forms.Form):
    duration_in_hour = forms.IntegerField(label='duration', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter duration of Booking'}))
