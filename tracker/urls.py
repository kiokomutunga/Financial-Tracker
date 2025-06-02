from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
]
