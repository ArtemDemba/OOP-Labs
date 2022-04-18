from datetime import date
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Month(models.Model):
    month_amount = models.PositiveSmallIntegerField(default=0)
    bank = models.ManyToManyField('Bank')

    def __str__(self):
        return str(self.month_amount)


class InterestRate(models.Model):
    interest_rate = models.FloatField(default=1)
    bank = models.ManyToManyField('Bank')

    def __str__(self):
        return str(self.interest_rate)


class User(AbstractUser):
    phone = models.CharField(max_length=13, default='', verbose_name='phone')
    passport_number = models.CharField(max_length=20, default='', verbose_name='passport number')
    blocked = models.BooleanField(default=False)
    banks = models.ManyToManyField('Bank')
    roles = (
        ('Client', 'Client'),
        ('Manager', 'Manager'),
        ('Administrator', 'Administrator'),
    )
    role = models.CharField(max_length=30, choices=roles, default=roles[0][1])
    reg_status = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accessed', 'accessed')
    )
    registration_status = models.CharField(max_length=30, choices=reg_status, default=reg_status[1][0])

    def is_blocked(self):
        return self.blocked

    def __str__(self):
        return self.username


class FinancialEntity(models.Model):
    class Meta:
        abstract = True

    sum = models.PositiveIntegerField(default=0)
    opening_date = models.DateField(auto_now_add=date.today())
    block = models.BooleanField(default=False)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)


class Transaction(models.Model):
    sending_sum = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=date.today())
    sender = models.ForeignKey('User', on_delete=models.CASCADE)
    recipient = models.ForeignKey('BankAccount', on_delete=models.CASCADE)


class BankAccount(FinancialEntity):
    frozen = models.BooleanField(default=False)

    def is_frozen(self):
        return self.frozen

    def is_blocked(self):
        return self.block

    def __str__(self):
        return f"Account Id: {self.pk}"


class Deposit(FinancialEntity):
    months = models.ForeignKey('Month', on_delete=models.PROTECT)
    interest_rate = models.ForeignKey('InterestRate', on_delete=models.PROTECT)
    appr = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted'),
    )
    approve = models.CharField(max_length=30, choices=appr, default=appr[1][0])


class Credit(FinancialEntity):
    months = models.ForeignKey('Month', on_delete=models.PROTECT)
    interest_rate = models.ForeignKey('InterestRate', on_delete=models.PROTECT)
    appr = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted'),
    )
    approve = models.CharField(max_length=30, choices=appr, default=appr[1][0])


class Installment(FinancialEntity):
    months = models.ForeignKey('Month', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    states = (
        ('denied', 'denied'),
        ('checking', 'checking'),
        ('accepted', 'accepted')
    )
    installment_status = models.CharField(max_length=200, choices=states, default=states[1][0])

    def __str__(self):
        return f"Installment of {self.user.username} - {self.sum} BYN"


class Enterprise(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=100, default='', unique=True)
    email = models.CharField(max_length=50, default='')
    PAN = models.CharField(max_length=9, unique=True, default='')
    address = models.CharField(max_length=150, unique=True, default='')


class Company(Enterprise):

    def __str__(self):
        return self.name


class Bank(Enterprise):
    BIC = models.CharField(max_length=9, unique=True, default='')

    def __str__(self):
        return self.name


class Applications(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=13, default='', verbose_name='phone')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class BankSpecialist(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=100, default='', unique=True)
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=13, default='', verbose_name='phone')
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    password = models.CharField(max_length=50, default='')


class Operator(BankSpecialist):

    def __str__(self):
        return self.name


class Manager(Operator):

    def __str__(self):
        return self.name
