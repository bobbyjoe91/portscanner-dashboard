from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(value, arg):
    """
    This function will retrieve status report
    by IP
    """
    data = value
    ip = arg

    return data[ip]
