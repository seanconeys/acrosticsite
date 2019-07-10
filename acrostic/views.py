from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Acrostic
# Create your views here.
def index(request):
     template = loader.get_template('acrostic/index.html')
     context = {}
     return render(request, 'acrostic/index.html', context)



def poem(request, acrostic_id):
    acrostic = get_object_or_404(Acrostic, pk=acrostic_id)
    template = loader.get_template('acrostic/poem.html')
    context = {
    'acrostic': acrostic
    }
    return render(request, 'acrostic/poem.html', context)

def create(request):
    root_word = request.POST['Root Word']
    acrostic = Acrostic.create(root_word)
    return HttpResponse(acrostic.poem.latest())
