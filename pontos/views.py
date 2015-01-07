# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.
from .forms import TimesheetForm, RegistrationForm, LoginForm
from .models import Timesheet

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

    template = 'registration.html'
    context = {'user_form': user_form, 'registered': registered}
    return render(request, template, context)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # username = request.POST['username']
        # password = request.POST['password']
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/mytimesheet')
                else:
                    # return HttpResponse("Conta inativa.")
                    error_message = "Conta inativa!"
                    login_form = LoginForm()
            else:
                # return HttpResponse("Usuário e ou senha inválidos")
                error_message = "Usuário e ou senha inválidos!"
                login_form = LoginForm()
        else:
            error_message = "O nome de usuário e a senha devem ser informadas para acessar!"
            login_form = LoginForm()

    else:
        error_message = False
        login_form = LoginForm()

    print "erro: '%s'" % error_message
    template = 'login.html'
    context = {'login_form': login_form, 'error_message': error_message}
    return render(request, template, context)

@login_required
def timesheet(request):
    registros = Timesheet.objects.filter(user=request.user).order_by('-registro')
    dashboard = {}
    status = {}
    for reg in registros:
        reg_date_str = reg.registro.strftime('%d/%m/%Y')
        if reg_date_str in dashboard:
            dashboard[reg_date_str].insert(0, reg)
            status[reg_date_str] = getStatus(dashboard[reg_date_str])
        else:
            dashboard[reg_date_str] = []
            dashboard[reg_date_str].insert(0, reg)
            status[reg_date_str] = 'Somente uma entrada'
    print dashboard
    print status


    template = 'timesheet.html'
    context = {'registros': registros}
    return render(request, template, context)

def getStatus(registros):
    registros_size = len(registros)

    if registros_size==1:
        return "Somente uma entrada"
    elif registros_size==2:
        return "retorno do almoço estimado para x"
    elif registros_size==3:
        return "saída estimada para x horas"
    elif registros_size==4:
        return "banco de horas de x horas"
    elif registros_size==5:
        return "retorno da janta estimado para x"
    elif registros_size==6:
        return "banco de horas de x horas (com janta)"

    return 'yada'


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def novo(request):
    if request.method=='POST':
        form=TimesheetForm(request.POST)
        if form.is_valid():
            registro=form.save(commit=False)
            registro.user=request.user
            registro.ip_address = get_ip(request)
            registro.save()
            return redirect('/mytimesheet/')
    else:
        form = TimesheetForm()

    context={"form": form}
    template = "novo.html"
    return render(request, template, context)

@login_required
def edit(request, pk):
    registro = get_object_or_404(Timesheet, pk=pk)
    if request.method == "POST":
        form = TimesheetForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.user = request.user
            registro.ip_address = get_ip(request)
            registro.save()
            return redirect('/mytimesheet/')
    else:
        form = TimesheetForm(instance=registro)

    context={"form": form}
    template = "edit.html"
    return render(request, template, context)

@login_required
def remove(request, pk):
    registro = get_object_or_404(Timesheet, pk=pk)
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