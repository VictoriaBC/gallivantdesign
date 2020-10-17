from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
	path('contact-me/', views.ContactMe.as_view(), name='contact-me'),
	path('download_image/', views.order_history, name='download_image'),
]