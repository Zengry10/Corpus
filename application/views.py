
from django.shortcuts import render
from .models import Corpus
from django.http import HttpResponse

def index(request):
    index_list = Corpus.objects.all()
    return render(request, 'application/index.html', {'index_list' : index_list})
    return HttpResponse('<h1>This is the profile page! The user is {}.</h1>'.format(username))

def profile(request, username="Default User"):
    return HttpResponse('<h1>This is the profile page! The user is {}.</h1>'.format(username))
# Create your views here.
 