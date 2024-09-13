from django.shortcuts import render
from datetime import datetime


time = datetime.now()
def main(request):

    return render(request, 'portfolio/main.html', {"time":time})


def about(request):
    return render(request, 'portfolio/about.html', {"time":time})


def contact(request):
    return render(request, 'portfolio/contact.html', {"time":time})

