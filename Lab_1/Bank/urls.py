from django.urls import path
from . import views


urlpatterns = [
    path('main_manager/', views.manager_page, name='main_manager'),
    path('main_manager/show_accounts_manager/edit/<int:id>/', views.block_acc),
    path('main_manager/show_accounts_manager/', views.show_bank_accounts_manager, name='show_accs_manager'),
    path('main_manager/show_deposits_manager/approve_deposit/<int:id>/', views.approve_deposit),
    path('main_manager/show_deposits_manager/', views.show_deposits_manager),
    path('main_manager/show_applications/', views.show_people_manager, name='show_applications'),
    path('main_manager/show_applications/edit/<int:id>/', views.approve_reg_status),

    path('main_operator/', views.operator_page, name='main_operator'),
    path('main_operator/show_accounts/', views.show_bank_accounts_operator, name='show_accs_operator'),
    path('main_operator/show_transactions_operator/', views.show_transactions_operator, name='show_transactions_operator'),

    path('main/', views.main_page, name='main'),
    path('main/add_bank_acc/', views.open_bank_account, name='addBankAcc'),
    path('main/show_bank_accs/', views.show_user_accounts, name='showBankAccs'),
    path('main/open_deposit/', views.open_deposit, name='openDeposit'),
    path('main/show_deposit/', views.show_deposits, name='showDeposits'),
    path('main/open_credit/', views.open_credit, name='openCredit'),
    path('main/open_installment/', views.open_installment, name='openInstallment'),
    path('main/show_installment/', views.show_installments, name='showInstallment'),
    path('main/transaction/', views.transaction, name='transaction'),
    path('main/show_my_transactions/', views.show_my_transactions, name='show_my_transactions'),

    path('', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.registration_page, name='registration'),

]
