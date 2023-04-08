from django.shortcuts import render, get_object_or_404, redirect
from filmyweb.models import Film, AdditionalInfo, Grade
from filmyweb.forms import MovieForm, AdditionalInfoForm, GradeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.


def all_movies(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    test = "To jest coś we views"
    filmy = Film.objects.all()

    buttons = []
    if request.user.is_authenticated:
        if request.resolver_match.url_name == 'all_movies':
            buttons.append({
                'text': 'Dodaj film',
                'url': reverse('new_movie'),
                'class': 'fa-solid fa-circle-plus',
            })
        buttons.append({
            'text': 'Wyloguj',
            'url': reverse('logout'),
        })
    else:
        buttons.append({
            'text': 'Zaloguj',
            'url': reverse('login'),
        })
    context = {
        'buttons': buttons,
        'text2': test,
        'filmy': filmy
    }
    return render(request, 'movies.html', context)


@login_required()
def new_movie(request):
    form_basic = MovieForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfoForm(request.POST or None)
    contex = {
        'form': form_basic,
        'form_additional': form_additional,
        'grade': None,
        'form_grade': None
    }

    if all((form_basic.is_valid(), form_additional.is_valid())):
        movie = form_basic.save(commit=False)
        additional = form_additional.save()
        movie.additional = additional
        movie.save()
        contex['success'] = True

    return render(request, 'new_edit_movie.html', contex)


@login_required()
def edit_movie(request, id):
    movie = get_object_or_404(Film, pk=id)
    grade = Grade.objects.filter(title=movie)
    actors = movie.Actors.all()
    try:
        additional = AdditionalInfo.objects.get(film=movie.id)
    except AdditionalInfo.DoesNotExist:
        additional = None

    form_basic = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    form_additional = AdditionalInfoForm(request.POST or None, instance=additional)
    form_grade = GradeForm(request.POST or None)

    if request.method == 'POST':
        grade = form_grade.save(commit=False)
        grade.title = movie
        grade.save()

    contex = {
        'form': form_basic,
        'form_additional': form_additional,
        'form_grade': form_grade,
        'grade': grade
    }

    if all((form_basic.is_valid(), form_additional.is_valid())):
        my_movie = form_basic.save(commit=False)
        additional = form_additional.save()
        my_movie.additional = additional
        my_movie.save()
        contex['success'] = True

    return render(request, 'new_edit_movie.html', contex)


@login_required()
def delete_movie(request, id):
    movie = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)
    return render(request, 'confirm_movie.html', {'movie': movie})

@login_required()
def review_movie(request, id):
    movie = get_object_or_404(Film, pk=id)
    grades = Grade.objects.filter(title=movie)

    if request.method == 'POST':
        form_grade = GradeForm(request.POST)
        if form_grade.is_valid():
            grade = form_grade.save(commit=False)
            grade.title = movie
            grade.user = request.user
            grade.save()
    else:
        form_grade = GradeForm()

    context = {
        'form_grade': form_grade,
        'grades': grades,
        'movie': movie
    }
    return render(request, 'reviews.html', context)

def my_buttons(request):
    buttons = []
    if request.user.is_authenticated:
        if request.resolver_match.url_name == 'all_movies':
            buttons.append({
                'text': 'Dodaj film',
                'url': reverse('new_movie'),
                'class': 'fa-solid fa-circle-plus',
            })
        buttons.append({
            'text': 'Wyloguj',
            'url': reverse('logout'),
        })
    else:
        buttons.append({
            'text': 'Zaloguj',
            'url': reverse('login'),
        })
    context = {
        'buttons': buttons,
    }
    return render(request, 'my_template.html', context)
