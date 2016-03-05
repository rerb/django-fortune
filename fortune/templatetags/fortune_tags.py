from django import template

from fortune.models import Fortune


register = template.Library()


@register.simple_tag
def fortune():
    return Fortune.fortune()
