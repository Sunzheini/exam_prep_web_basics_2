from django.contrib import admin

from exam_prep_web_basics_2.my_music_app.models import Album, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

