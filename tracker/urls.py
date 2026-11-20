from django.urls import path
from .views import dashboard, delete_expense

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path(
        'delete/<int:id>/',
        delete_expense,
        name='delete_expense'
    ),
]