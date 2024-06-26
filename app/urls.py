from django.contrib import admin
from django.urls import path
from genres.views import genre_list_view, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list_view, name = 'genre-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre_detail_view'),
]
