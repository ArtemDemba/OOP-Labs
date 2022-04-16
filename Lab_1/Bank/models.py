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


class BankAccount(FinancialEntity):
    frozen = models.BooleanField(default=False)

    def is_frozen(self):
        return self.frozen

    def is_blocked(self):
        return self.block


class Deposit(FinancialEntity):
    month = ((3, 3),
             (6, 6),
             (9, 9),
             (12, 12),
             (24, 24),
             (36, 36))
    credit_status = models.PositiveSmallIntegerField(choices=month, default=month[1][0])
    interest_rate = models.ForeignKey('InterestRate', on_delete=models.PROTECT)


class Credit(Deposit):
    pass


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
