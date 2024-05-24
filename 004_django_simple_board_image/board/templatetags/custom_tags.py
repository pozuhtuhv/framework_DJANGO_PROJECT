import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def parse_content(value):
    image_pattern = re.compile(r'\[이미지:(.+?)\]')
    parts = image_pattern.split(value)
    
    result = []
    for part in parts:
        if part.startswith('images/'):
            img_tag = f'<img src="/media/{part}" alt="Uploaded Image">'
            result.append(img_tag)
        else:
            result.append(part)
    
    return mark_safe(''.join(result))
