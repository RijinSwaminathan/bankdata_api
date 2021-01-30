from django.urls import path

from bank import views

urlpatterns = [
    path('get-bank-by-ifsc/', views.BankDetailsByIFSC.as_view(), name='get_by_ifsc'),
    path('get-bank-by_name/', views.BankDetailsByName.as_view(), name='get_by_name_city')
]
