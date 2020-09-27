from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('', views.all_products, name='illustrations'),
    path('', views.all_products, name='services'),
    path('', views.all_products, name='showcase')
]