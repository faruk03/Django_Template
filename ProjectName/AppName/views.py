from django.shortcuts import render
from AppName.models import *
# Create your views here.

def index(request):
    users = user.objects.all()
    test = True
    return render(request, 'teacher/teachers.html', {'users': users,
    'test': test})