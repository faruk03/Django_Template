from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('submit/', submit, name='submit'),
    path('sql_test/', sql_test, name = 'sql_test'),
]
