from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def mypage(request):
    return render(request,'generator/mypage.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('number'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    length = int(request.GET.get('length',12))

    thepassword=''

    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html', {'password' : thepassword})
