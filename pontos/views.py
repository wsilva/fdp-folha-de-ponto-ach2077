# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.
from .forms import RegistroForm, RegistrationForm
from .models import Registro

def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = RegistrationForm()

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
                return redirect('/mytimesheet')
            else:
                return HttpResponse("Conta inativa.")
        else:
            return HttpResponse("Usuário e ou senha inválidos")
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
    return redirect('/')

@login_required
def novo(request):
    if request.method=='POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            registro=form.save(commit=False)
            registro.user=request.user
            registro.ip_address = get_ip(request)
            registro.save()
            return redirect('/mytimesheet/')
    else:
        form = RegistroForm()

    context={"form": form}
    template = "novo.html"
    return render(request, template, context)

@login_required
def edit(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == "POST":
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.user = request.user
            registro.ip_address = get_ip(request)
            registro.save()
            return redirect('/mytimesheet/')
    else:
        form = RegistroForm(instance=registro)

    context={"form": form}
    template = "edit.html"
    return render(request, template, context)

@login_required
def remove(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    registro.delete()
    return redirect('/mytimesheet/')

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