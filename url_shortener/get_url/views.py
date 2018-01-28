import re
import string
import random

from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict

from .models import URLMapping

# Create your views here.
def index(request):
    return render(request, "get_url/index.html")

def createMapping(request, original_url):
    mapping_letters = random.choices(string.ascii_letters + string.digits, k=6)
    mapping_string = ''.join(mapping_letters)
    u_map = URLMapping(original_url=original_url,
                       mapping_string=mapping_string,
                       short_url='{}/{}'.format(request.get_host(), mapping_string))
    u_map.save()
    context = {
        "u_map": model_to_dict(u_map)
    }
    return render(request, "get_url/mapping.html", context)

def redirectToOrigin(request, mapping_string):
    u_map = URLMapping.objects.get(mapping_string=mapping_string)
    original_url = u_map.original_url
    p = re.compile(r'^(?:http|https)://.+?$')
    if p.match(original_url):
        pass
    else:
        original_url = 'https://{}'.format(original_url)
    return redirect(original_url)
