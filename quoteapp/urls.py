from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('quote/', quote_page, name='quote_page'),
    path('api/quote/', random_quote, name='random_quote'),
    path('api/search/', search_quote, name='search_quote'),
]
