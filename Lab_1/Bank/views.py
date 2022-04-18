from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def block_acc(request, id):
    acc = BankAccount.objects.get(id=id)

    if request.method == "POST":
        acc.block = request.POST.get("block")

        acc.save()

        return redirect("/main_manager/")
    else:
        return render(request, "Bank/edit_bank_acc.html", {"acc": acc})


def approve_reg_status(request, id):
    p = User.objects.get(id=id)

    if request.method == "POST":
        p.registration_status = request.POST.get("registration_status")

        p.save()

        return redirect("/main_manager/")
    else:
        return render(request, "Bank/approve_reg_status.html", {"p": p})


def approve_deposit(request, id):
    dep = Deposit.objects.get(id=id)

    if request.method == "POST":
        dep.approve = request.POST.get("approve")

        dep.save()

        return redirect("/main_manager/")
    else:
        return render(request, "Bank/approve_deposit.html", {"dep": dep})


def open_bank_account(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
    else:
        form = BankAccountForm()

    if request.user.is_blocked():
        return HttpResponse('You can`t open bank account because you are blocked')

    return render(request, 'Bank/open_account.html', {'form': form, 'title': 'Open account'})


@login_required(login_url='login')
def open_deposit(request):

    if request.method == 'POST':
        form = DepositForm(request.POST)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
    else:
        form = DepositForm()

    if request.user.is_blocked():
        return HttpResponse('You can`t open deposit because you are blocked')

    return render(request, 'Bank/open_deposit.html', {'form': form, 'title': 'Open deposit'})


@login_required
def show_user_accounts(request):
    accs = BankAccount.objects.filter(user=request.user)
    context = {'accs': accs, 'title': 'Show accounts'}
    return render(request, 'Bank/show_users_accounts.html', context)


@login_required
def show_deposits(request):
    deposits = Deposit.objects.filter(user=request.user)
    context = {'deposits': deposits, 'title': 'Show deposit'}
    return render(request, 'Bank/show_deposits.html', context)


@login_required
def show_deposits_manager(request):
    deposits = Deposit.objects.all()
    context = {'deposits': deposits, 'title': 'Show deposits for manager'}
    return render(request, 'Bank/show_deposits_manager.html', context)


@login_required
def show_installments(request):
    inst = Installment.objects.filter(user=request.user)
    context = {'inst': inst, 'title': 'Show installments'}
    return render(request, 'Bank/show_installments.html', context)


@login_required(login_url='login')
def open_credit(request):

    if request.method == 'POST':
        form = CreditForm(request.POST)

        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
    else:
        form = CreditForm()

    if request.user.is_blocked():
        return HttpResponse('You can`t open credit because you are blocked')

    return render(request, 'Bank/open_credit.html', {'form': form})


@login_required(login_url='login')
def open_installment(request):

    if request.method == 'POST':
        form = InstallmentForm(request.POST)

        if form.is_valid():
            installment = form.save(commit=False)
            installment.user = request.user
            installment.save()
    else:
        form = InstallmentForm()

    if request.user.is_blocked():
        return HttpResponse('You can`t open installment because you are blocked')

    return render(request, 'Bank/open_installment.html', {'form': form})


@login_required(login_url='login')
def transaction(request):
    if not BankAccount.objects.all()[0]:
        return HttpResponse('There aren\'t bank accounts!')
    else:
        bank_acc_form = TransactionForm()
        sender_acc = BankAccount.objects.all().get(user=request.user)
        if request.method == 'POST':
            bank_acc_form = TransactionForm(request.POST)

            if bank_acc_form.is_valid():
                bank_acc_form = TransactionForm(request.POST)
                transact = bank_acc_form.save(commit=False)
                transact.sender = request.user
                data = bank_acc_form.cleaned_data
                acc = data['recipient']
                sending_sum = data['sending_sum']

                if sending_sum > sender_acc.sum:
                    return HttpResponse('Not enough money')
                if acc == sender_acc:
                    return HttpResponse('Error! You can\'t transfer money to yourself')

                sender_acc.sum -= sending_sum
                sender_acc.save()
                acc.sum += sending_sum
                acc.save()
                transact.save()

        context = {
            'form': bank_acc_form,
            'sender_acc': sender_acc,
            'title': 'Transaction'
        }

        if request.user.is_blocked():
            return HttpResponse('You can`t make transaction because you are blocked')

        return render(request, 'Bank/transaction.html', context)


def show_my_transactions(request):
    transactions = Transaction.objects.filter(sender=request.user)
    context = {'transactions': transactions, 'title': 'Show my transactions'}
    return render(request, 'Bank/show_transactions.html', context)


@login_required
def show_transactions_operator(request):
    transact = Transaction.objects.all()
    context = {'transactions': transact, 'title': 'Show transactions for operator'}

    return render(request, 'Bank/show_all_transactions.html', context)


def main_page(request):
    return render(request, 'Bank/main_customer.html', {'title': 'Main page'})


def main_manager(request):
    return render(request, 'Bank/main_customer.html', {'title': 'Main manager page'})


def registration_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form, 'title': 'Registration'}

    return render(request, 'Bank/registrate.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.registration_status == 'denied':
                        return HttpResponse('Your registration is denied')
                    if user.registration_status == 'checking':
                        return HttpResponse('Your registration is checking')
                    if user.registration_status == 'accessed':
                        if request.user.role == 'Client':
                            return redirect('main/')
                        if request.user.role == 'Operator':
                            return redirect('main_operator/')
                        if request.user.role == 'Manager':
                            return redirect('main_manager/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'Bank/login.html', {'form': form, 'title': 'Login'})


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def operator_page(request):
    context = {'title': 'Main operator page'}

    return render(request, 'Bank/operator_page.html', context)


@login_required
def manager_page(request):
    context = {'title': 'Main manager page'}

    return render(request, 'Bank/manager_page.html', context)


@login_required
def show_people_manager(request):
    pers = User.objects.filter(registration_status='checking')
    context = {'pers': pers, 'title': 'Show applications for operator'}

    return render(request, 'Bank/show_people_manager.html', context)


@login_required
def show_bank_accounts_operator(request):
    accs = BankAccount.objects.all()
    context = {'accs': accs, 'title': 'Show accounts for operator'}

    return render(request, 'Bank/show_all_accounts.html', context)


@login_required
def show_bank_accounts_manager(request):
    accs = BankAccount.objects.all()
    context = {'accs': accs, 'title': 'Show accounts for operator'}

    return render(request, 'Bank/show_accounts_manager.html', context)
