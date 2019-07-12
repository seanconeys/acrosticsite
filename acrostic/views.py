from django.shortcuts import render, loader, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Acrostic
from django.urls import reverse
import json


def index(request):
     template = loader.get_template('acrostic/index.html')
     context = {}
     return render(request, 'acrostic/index.html', context)



def poem(request, acrostic_id):
    acrostic = get_object_or_404(Acrostic, pk=acrostic_id)
    template = loader.get_template('acrostic/poem.html')
    poem = json.decoder.JSONDecoder().decode(acrostic.poem)
    context = {
    'acrostic': acrostic,
    'poem': poem,
    }
    return render(request, 'acrostic/poem.html', context)

def create(request):
    try:
        root_word = request.POST['Root Word']
        acrostic = Acrostic.create(root_word)
        return HttpResponseRedirect(reverse('acrostic:poem', args=(acrostic.id,)))

    except:
        return render(request, 'acrostic/index.html', {
        'error_message': "No numbers or special characters are allowed",
        })
