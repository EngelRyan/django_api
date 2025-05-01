from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_min_data(date):
    if date > timezone.now().date():
        raise ValidationError(
            "Data maior que hoje não né",
            params={"date": date},
        )