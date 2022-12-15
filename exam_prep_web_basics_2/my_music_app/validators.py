from django.core.exceptions import ValidationError

"""
The username can consist only of letters, numbers, and underscore ("_"). 
Otherwise, raise a ValidationError with the message: "Ensure this value 
contains only letters, numbers, and underscore."
"""


def text_validator(value):
    for i in value:
        if not i.isalnum() and i != '_':
            raise ValidationError("Ensure this value contains only letters, "
                                  "numbers, and underscore.")


def float_above_zero(value):
    if value < 0.0:
        raise ValidationError("Cannot be below 0.0")
