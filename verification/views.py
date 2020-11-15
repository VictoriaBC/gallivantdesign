from django.shortcuts import render

# Create your views here.
from verify_email.email_handler import send_verification_link

def register_user(request):
    ...

    if form.is_valid():

        inactive_user = send_verification_link(request, form)

inactive_user.cleaned_data['email']

# Output : victoriapben@gmail.com