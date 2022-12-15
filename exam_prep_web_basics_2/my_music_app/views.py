from django.shortcuts import render, redirect
from exam_prep_web_basics_2.my_music_app.forms import ProfileForm
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
    return render(request, 'albums/add-album.html')


def album_details(request, pk):
    return render(request, 'albums/album-details.html')


def edit_album(request, pk):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk):
    return render(request, 'albums/delete-album.html')


def profile_details(request):
    return render(request, 'profiles/profile-details.html')


def profile_delete(request):
    return render(request, 'profiles/profile-delete.html')





