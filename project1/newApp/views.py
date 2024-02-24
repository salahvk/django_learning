from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def print_hello(request):
    personal_details={
     'name':'salah',
     'age':'22',
     'company':'viewy',
    }
    return render(request,"hello.html",personal_details)