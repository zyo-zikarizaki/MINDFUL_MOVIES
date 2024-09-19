from django.urls import path
from . import views


urlpatterns = [
    path('', views.search_movies, name='search_movies'),  # 映画検索
    path('now-playing/', views.now_playing_movies, name='now_playing_movies'),  # 公開中の映画
    path('upcoming_movies/', views.upcoming_movies, name='upcoming_movies'),
]

