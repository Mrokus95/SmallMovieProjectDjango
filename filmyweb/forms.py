from django.forms import ModelForm
from .models import Film, AdditionalInfo, Grade

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