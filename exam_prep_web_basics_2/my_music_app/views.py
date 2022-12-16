from django.shortcuts import render, redirect
from exam_prep_web_basics_2.my_music_app.forms import ProfileForm, AlbumForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from exam_prep_web_basics_2.my_music_app.models import Profile, Album


# --------------------------------------------------------------------------
# profile / no profile different homepage


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


# --------------------------------------------------------------------------

def add_album(request):

    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'albums/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):

    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):

    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-delete.html', context)





