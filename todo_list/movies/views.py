import requests
from django.conf import settings
from django.shortcuts import render

def search_movies(request):
    query = request.GET.get('query')  # 検索クエリ
    movies = []
    if query:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}&language=ja"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            movies = data.get('results', [])
    
    return render(request, 'movies/search.html', {'movies': movies})

def now_playing_movies(request):
    # TMDBの「公開中の映画」エンドポイント
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={settings.TMDB_API_KEY}&language=ja&region=JP"
    response = requests.get(url)
    movies = []
    
    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])

    return render(request, 'movies/now_playing.html', {'movies': movies})

def upcoming_movies(request):
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={settings.TMDB_API_KEY}&language=ja&region=JP"
    response = requests.get(url)
    movies = []
    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])
    
    return render(request, 'movies/upcoming_movies.html', {'movies': movies})
