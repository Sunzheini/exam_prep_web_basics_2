from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from exam_prep_web_basics_2.my_music_app.views \
    import index, add_album, album_details, edit_album, \
    delete_album, profile_details, profile_delete, add_profile


urlpatterns = [
    # http://localhost:8000/
    path('', index, name='index'),

    path('album/', include([
        # http://localhost:8000/album/add/
        path('add/', add_album, name='add album'),
        # http://localhost:8000/album/details/<id>/
        path('details/<int:pk>/', album_details, name='album details'),
        # http://localhost:8000/album/edit/<id>/
        path('edit/<int:pk>/', edit_album, name='edit album'),
        # http://localhost:8000/album/delete/<id>/
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),

    path('profile/', include([
        path('add/', add_profile, name='add profile'),

        # http://localhost:8000/profile/details/
        path('details/', profile_details, name='profile details'),
        # http://localhost:8000/profile/delete/
        path('delete/', profile_delete, name='profile delete'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
