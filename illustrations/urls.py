from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_illustrations, name='illustrations'),
    path('<product_id>', views.product_detail, name='product_detail'),
]