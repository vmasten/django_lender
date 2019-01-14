from django.utils import timezone
from django import template
from datetime import timedelta


register = template.Library()


@register.filter
def get_due_date(value):
    """Get the date and filter it."""
    due_date = value + timedelta(days=14)
    delta = due_date - value

    if delta.days == 0:
        return 'today!'
    elif delta.days < 1:
        return f'{abs(delta.days)} { "day" if abs(delta.days) == 1 else "days" } ago!'
    elif delta.days == 1:
        return 'tomorrow'
    elif delta.days > 1:
        return f'in {delta.days} days'
    else:
        return 'you should not be here.'
