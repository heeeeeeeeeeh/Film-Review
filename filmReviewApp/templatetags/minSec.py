# myapp/templatetags/duration_filters.py
from django import template

register = template.Library()


@register.filter
def min_sec(value):
    """Convert a timedelta to MM:SS format."""
    total_seconds = int(value.total_seconds())
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"
