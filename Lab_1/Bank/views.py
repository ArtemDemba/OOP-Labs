from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def open_bank_account(request):
    if request.method == 'POST':
        form = BankAccountForm()
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
    else:
        form = BankAccountForm()

    if request.user.is_blocked():
        return HttpResponse('You can`t open bank account because you are blocked')

    return render(request, 'Bank/open_account.html', {'form': form})


def main(request):
    return render(request, 'Bank/main_customer.html')


def registration_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}

    return render(request, 'Bank/registrate.html', context)


def register_bank_spec(request):
    form = RegisterBankSpec()

    if request.method == 'POST':
        form = RegisterBankSpec(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}

    return render(request, 'Bank/register_bank_spec.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'Bank/login.html', {'form': form})


def operator_page(request):
    accounts = BankAccount.objects.all()
    context = {'accounts': accounts, 'bank': Manager.bank}

    return render(request, 'Bank/operator.html', context)


def login_bank_spec(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'Bank/login_bank_specialist.html', {'form': form})
