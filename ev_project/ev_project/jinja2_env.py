from jinja2 import Environment
from django.templatetags.static import static
from django.urls import reverse
from django.middleware.csrf import get_token

def url(viewname, *args, **kwargs):
    if kwargs:
        return reverse(viewname, kwargs=kwargs)
    if args:
        return reverse(viewname, args=args)
    return reverse(viewname)

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': url,
        'csrf_token': get_token,
    })
    return env
