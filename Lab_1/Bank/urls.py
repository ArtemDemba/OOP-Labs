from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.registration_page, name='registration'),
    path('register_bank_spec/', views.register_bank_spec, name='register_bank_spec'),
    path('login/', views.login_page, name='login'),
    path('login_bank_spec/', views.login_bank_spec, name='login_bank_spec'),
    path('add_bank_acc/', views.open_bank_account, name='addBankAcc'),
    path('show_bank_accs/', views.show_user_accounts, name='showBankAccs'),
    path('open_deposit/', views.open_deposit, name='openDeposit'),
    path('show_deposit/', views.show_deposits, name='showDeposits'),
    path('open_credit/', views.open_credit, name='openCredit'),
]
