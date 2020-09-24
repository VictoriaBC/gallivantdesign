from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', views.all_products, name='illustrations'),
    path('', views.all_products, name='services'),
    path('', views.all_products, name='showcase')
]