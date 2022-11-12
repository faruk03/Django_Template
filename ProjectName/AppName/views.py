from django.shortcuts import render

# Create your views here.

def index(request):
    name = 'faruk'
    test = True
    return render(request, 'index.html', {'name': name,
                                          'test': test})