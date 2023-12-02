from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_years(value):
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            f'{value} год не должен быть больше {now}'
        )
