from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserBase
from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=255, help_text='Required', error_messages={
                             'required': 'Email required.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    contact_number = PhoneNumberField(label='Phone Number', help_text='Required', error_messages={
                                      'required': 'contact number required.'}, region='US')

    class Meta:
        model = UserBase
        fields = ('user_name', 'email', 'contact_number')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        if UserBase.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
        self.fields['contact_number'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': '123-456-7890'}
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'login-pwd'}))
