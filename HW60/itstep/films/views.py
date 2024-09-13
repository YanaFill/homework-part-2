from .data import films
from django.shortcuts import render

def main(request):
    sort_param = request.GET.get('sort')

    if sort_param:
        try:
            key, order = sort_param.split(':')
            if key in ['id', 'title', 'year', 'genre'] and order in ['asc', 'desc']:
                reverse = True if order == 'desc' else False
                sorted_films = sorted(films, key=lambda x: x[key], reverse=reverse)
            else:
                sorted_films = films
        except ValueError:
            sorted_films = films
    else:
        sorted_films = films

    return render(request, 'films/main.html', {'films':sorted_films, 'titile': 'main'})


def about_film(request, id):
    film = next((film for film in films if film["id"] == id), None)
    if not film:
        return render(request, "films/404.html", status=404)
    return render(request, 'films/about_film.html', {'film':film})

def filter_film(request):
    genre = request.GET.get('genre')
    year = request.GET.get('year')
    filtered_films = []
    for film in films:
        if film["genre"] == genre and film["year"] == int(year):
            filtered_films.append(film)
            print(film)
    print(genre, year)
    print(filtered_films)
    if not filtered_films:
        return render(request, "films/404.html", status=404)

    return render(request, "films/main.html", {"films": filtered_films, "title": "Filtered films"})

def filter_form(request):
    return render(request, "films/filter_form.html")