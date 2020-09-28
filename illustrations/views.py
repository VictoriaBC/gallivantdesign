from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_illustrations(request):
    """ A view to show all illustrations, including sorting and search queries """

    illustrations = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('illustrations'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            illustrations = illustrations.filter(queries)

    context = {
        'illustrations': illustrations,
        'search_term': query,
    }

    return render(request, 'illustrations/illustrations.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'illustrations/product_detail.html', context)