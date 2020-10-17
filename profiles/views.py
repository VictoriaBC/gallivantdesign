from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, ContactMeForm
from checkout.models import Order
from django.views.generic import View

class ContactMe(View):

	def post(self, request):
		form = ContactMeForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			# Send an email to typed in address
			send_mail(
				f'You sent a message to Victoria',
				f'Thanks for reaching out! We will be in touch soon.\n\n Message: "{message}"',
				'victoriapben@gmail.com',
				[email],
				fail_silently=True,
			)

			# Send an email to admin to notify him of a new message
			send_mail(
				f'You have a new message from {email}',
				f'Message: {message}',
				'victoriapben@gmail.com',
				['victoriapben@gmail.com'],
				fail_silently=True,
			)

			form.save()

			messages.info(request, "Message sent!")
			return redirect(reverse('home'))

		messages.error(request, "Invalid form")
		return redirect(reverse('contact-me'))


	def get(self, request):
		form = ContactMeForm()

		return render(request, 'contact-me.html', {'form': form})


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

