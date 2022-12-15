from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from exam_prep_web_basics_2.my_music_app.validators import text_validator, float_above_zero


class Profile(models.Model):

    profile_username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            text_validator,
        ),
        blank=False, null=False,
    )

    profile_email = models.EmailField(
        blank=False, null=False,
    )

    profile_age = models.PositiveIntegerField(
        blank=True, null=True,
    )


class Album(models.Model):

    class Meta:
        ordering = ['pk']

    album_name = models.CharField(
        max_length=30,
        unique=True,
        blank=False, null=False,
    )

    album_artist = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    album_genre = models.CharField(
        max_length=30,
        choices=(
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music",  "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other"),
        ),
        blank=False, null=False,
    )

    album_description = models.TextField(
        blank=True, null=True,
    )

    album_image_url = models.URLField(
        blank=False, null=False,
    )

    album_price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
        blank=False, null=False,
    )
