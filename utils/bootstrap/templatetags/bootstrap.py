from django.template import Context
from django.template.loader import get_template
from django import template
from django.http import QueryDict

register = template.Library()


@register.filter
def bootstrap(element, args=None):
    element_type = element.__class__.__name__.lower()
    #print element_type
    qs = QueryDict(args)
    #if element_type == 'boundfield':
    template = get_template('field.html')
    context = Context({'field': element})
    for k in qs:
        context[k] = qs.get(k)

    return template.render(context)


@register.filter
def render(element, args=None):
    return '<input id="{{ field.auto_id }}" name="{{ field.name }}" type="{{ field.field.widget.input_type }}"{% if field.field.required %} class="required"{% endif %}{% if field.placeholder %} placeholder="{% trans field.placeholder %}"{% endif %}{% if field.value %} value="{{ field.value }}"{% endif %}$attrs$/>'


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"
