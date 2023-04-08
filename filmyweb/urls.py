"""filmy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from filmyweb.views import all_movies, new_movie, edit_movie, delete_movie

urlpatterns = [
    path('all/', all_movies, name="all_movies"),
    path('new/', new_movie, name="new_movie"),
    path('edit/<int:id>/', edit_movie, name="edit_movie"),
    path('delete/<int:id>/', delete_movie, name="delete_movie")
]

