from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Illustration

# Create your views here.

def all_illustrations(request):
    """ A view to show all illustrations, including sorting and search queries """

    illustrations = Illustration.objects.all()
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


def illustration_detail(request, illustration_id):
    """ A view to show individual product details """

    product = get_object_or_404(Illustration, pk=illustration_id)

    context = {
        'illustration': all_illustrations,
    }

    return render(request, 'illustrations/illustration_detail.html', context)