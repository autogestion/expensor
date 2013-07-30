# encoding: utf-8
from __future__ import absolute_import
from django import forms
from .models import Person, Account


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('amount',)
