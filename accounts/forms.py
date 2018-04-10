from django.forms import ModelForm,CharField,PasswordInput,ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from accounts.models import User
from django import forms

class RegistrationForm(ModelForm):
    password = CharField(widget=PasswordInput)
    password2 = CharField(label='Confirm Password',widget=PasswordInput)

    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','bio','profession')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.get(email=email)
        if user.exists():
            raise ValidationError('Email id already taken')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.get(username=username)
        if user.exists():
            raise ValidationError('Username taken')
        return username

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('Passwords don\'t match')
        return pass2

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]
