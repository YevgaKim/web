import base64

import requests
from django import template

register = template.Library()

@register.filter
def get_base64(content):
    encoded = base64.b64encode(content)
    return encoded.decode('utf-8')