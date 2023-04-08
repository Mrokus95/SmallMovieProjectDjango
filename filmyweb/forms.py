from django.forms import ModelForm
from .models import Film, AdditionalInfo, Grade
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MovieForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title','year','type','director','description','release_date','imdb_rating','poster']

class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['duration', 'watched', 'movie_type']

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['review', 'grade']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user