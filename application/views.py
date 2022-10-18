
from django.shortcuts import render
from .models import Corpus

def index(request):
    index_list = Corpus.objects.all()
    return render(request, 'application/index.html', {'index_list' : index_list})
# Create your views here.
 