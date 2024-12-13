from django import template

register = template.Library()

@register.simple_tag
def generate_range(start, end):
    """
    Generate a range of numbers (inclusive).
    Usage: {% generate_range start end %}
    """
    return range(start, end + 1)
