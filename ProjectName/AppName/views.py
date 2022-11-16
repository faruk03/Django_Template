from django.shortcuts import render, redirect
from AppName.models import *
# Create your views here.

def index(request):
    users = user.objects.all()
    test = True
    return render(request, 'teacher/teachers.html', {'users': users,
    'test': test})
    
def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        t = user.objects.create(name = name, age = age, email = email)
        t.save()
        return redirect(index)
    return render(request, 'teacher/submit.html')