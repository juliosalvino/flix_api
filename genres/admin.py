from django.contrib import admin
from genres.models import genre


@admin.register(genre)
class genreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

