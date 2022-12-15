from django import forms
from exam_prep_web_basics_2.my_music_app.models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

