from django.urls import path
from .views import book_registr

urlpatterns = [
    path('', book_registr, name='book_registr'),
]
