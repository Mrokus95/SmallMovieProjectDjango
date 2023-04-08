from django.contrib import admin
from .models import Film, AdditionalInfo, Grade, Actor


# Register your models here.

# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):

    # fields = ["title", "description", "year"] #wybieramy ręcznie pola, które mają zostać pokazane z modelu
    # exclude = ["description"] # pokaże wszystkie pola poza tymi
    list_display = ['id', "title", "year", "imdb_rating", 'poster']  # tworzy listę kolum do podglądu w aplikacji zamiast standardowego str
    list_filter = ["year", "imdb_rating"]  # Dodaje pole filtru po prawej stronie ekranu, można stosować kilka filtrów
    search_fields = ["title"]  # dodaje pole do wyszukiwania po polach tytuł, dodanie innych pól zwiększa zakres przeszukiwania


admin.site.register(AdditionalInfo)
admin.site.register(Grade)
admin.site.register(Actor)