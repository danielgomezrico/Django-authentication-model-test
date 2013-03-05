from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def main_page(request):
    return render_to_response('/people/index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/registration/login')