from django.db import models

class AdditionalInfo(models.Model):
    MOVIE_TYPE = {
        (0, 'Unknown'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sci-fi'),
        (4, 'Fantasy'),
        (5, 'Action'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    watched = models.BooleanField(blank=False, default=False)
    movie_type = models.PositiveSmallIntegerField(default=0, choices=MOVIE_TYPE)

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    type = models.CharField(max_length=255, blank=False, unique=False, default="")
    director = models.CharField(max_length=255, blank=False, unique=False, default="")
    description = models.TextField(default="")
    release_date = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f'{self.title} ({self.year})'

class Grade(models.Model):
    review = models.TextField(default="", blank=True)
    grade = models.PositiveSmallIntegerField(default=5)
    title = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    titles = models.ManyToManyField(Film, related_name="Actors")