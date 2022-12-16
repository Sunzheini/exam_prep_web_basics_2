from django import forms
from exam_prep_web_basics_2.my_music_app.models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'album_artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'album_description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'album_image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'album_price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance



