from django import forms
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'please enter user name'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Username or password is incorrect')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data



class RegForm(forms.Form):
    firstname = forms.CharField(label='firstname', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter firstname'}))
    lastname = forms.CharField(label='lastname', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter lastname'}))
    username = forms.CharField(label='username', max_length=30, min_length=3, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter 3-30 usernames'}))
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email-id'}))
    password = forms.CharField(label='password', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password_again = forms.CharField(label='Re-enter password', min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    user_phone = forms.CharField(label=u'cellphone number', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': ' Phone Number'}))
    car_number = forms.CharField(label=u'number plate', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please enter the license plate number'}))

    def clean_username(self):
        print("inside clean_username")
        username = self.cleaned_data.get('username')
        # print(username)
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        print("clean_username completed")
        return username

    def clean_email(self):
        print("inside email")
        email = self.cleaned_data.get('email')
        print(email)
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exits')

        print("clean_email completed")
        return email

    def clean_password_again(self):
        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')
        if password != password_again:
            raise forms.ValidationError('Inconsistent password entered twice')

        print("clean_password_again completed")

        return password_again





