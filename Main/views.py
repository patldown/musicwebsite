from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse

# Create your views here.
def index(request):
    context = dict()
    handle = open('Main/settings.txt', 'r')
    reader = handle.readlines()
    last_var = ''
    for line in reader:
        if "|" not in line and last_var != '':
            context[last_var] = context[last_var] + line.strip()
        else:
            line = line.strip()
            line = line.split("|")
            if line[0] != 'Musician_Name' and line[0] != 'Subscribe_Embed' :
                context[line[0]] = [line[1]]
            else:
                context[line[0]] = line[1]
            last_var = line[0]

    return render(request, 'Main/index.html', context)
