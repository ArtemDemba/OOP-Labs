from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Bank)
admin.site.register(Manager)
admin.site.register(BankAccount)
admin.site.register(Month)
admin.site.register(InterestRate)



