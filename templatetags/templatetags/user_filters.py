from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Template filter for adding html classes"""

    return field.as_widget(attrs={'class': css})
