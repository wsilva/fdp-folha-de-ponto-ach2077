# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from .forms import RegistroForm, UserForm
from .models import Registro

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(
        request,
        'registration.html',
        {'user_form': user_form, 'registered': registered}
    )

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/mytimesheet')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Credenciais da acesso invalidas: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})

@login_required
def timesheet(request):
    registros = Registro.objects.filter(user=request.user).order_by('-registro')
    return render(
        request,
        'timesheet.html',
        {'registros': registros}
    )

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def novo(request):
    if request.method=='POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            registro=form.save(commit=False)
            registro.user=request.user
            registro.ip_address = get_ip(request)
            registro.save()
            return HttpResponseRedirect('/mytimesheet/')
    else:
        form = RegistroForm()

    context={"form": form}
    template = "novo.html"
    return render(request, template, context)

def home(request):
    context={}
    template = "home.html"
    return render(request, template, context)

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip