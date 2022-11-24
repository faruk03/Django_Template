from django.shortcuts import render, redirect
from AppName.models import *

from django.db import connection  #for connecting with sql
from django.http import HttpResponse

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
        return redirect(index)#--> redirects to index function
    return render(request, 'teacher/submit.html')

# Search function should be implemented but I haven't understood this yet


#Now conecting with sql --> we are checking sql(commands) in django 
def sql_test(request):
    cursor = connection.cursor()
    sql = 'SELECT * FROM AppName_user'
    cursor.execute(sql)
    result = cursor.fetchall()
    #print(result)--> return array oof tuple, so lets iterate it
    for row in result:
        print(row)
    return HttpResponse('<h1>Hello World<h1/>')   
    
    
    
    