from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_illustrations, name='illustrations'),
    path('<illustration_id>', views.illustration_detail, name='illustration_detail'),
]