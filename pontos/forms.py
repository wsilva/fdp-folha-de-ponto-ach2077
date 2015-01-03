# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields=['registro',]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("A senha e a confirmação estão diferente.")
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user