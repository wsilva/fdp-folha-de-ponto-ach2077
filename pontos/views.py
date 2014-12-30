# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from .forms import RegistroForm, RegistroPontoForm, UserForm
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
    return render(
        request,
        'timesheet.html'
    )

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def novo(request):

    form = RegistroForm(request.POST or None)
    if form.is_valid():
        registro = form.cleaned_data['registro']
        new_registro, created = Registro.objects.get_or_create(registro=registro)
        print new_registro, created
        print new_registro.criado_em
        if created:
            print "Registro criado!"

    context={"form": form}
    template = "novo.html"
    return render(request, template, context)

def novoponto(request):

    form = RegistroPontoForm(request.POST or None)
    if form.is_valid():
        new_registro = form.save(commit=False)
        registro = form.cleaned_data['registro']
        new_registro_old, created = Registro.objects.get_or_create(registro=registro)
        # new_registro.save()

    context={"form": form}
    template = "novo.html"
    return render(request, template, context)

def home(request):
    context={}
    template = "home.html"
    return render(request, template, context)