from django.shortcuts import render
from .models import *

from django.db.models import Q
from django.views.generic import TemplateView
from django.views.generic.list import ListView



#на главной странице есть еще и категории
def home(request):
    return render(
        request, 'base.html', {
            'categories': Category.objects.all()
        }
    )


class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(Q(key__icontains=query))
        return object_list


#products
def products(request):
    return render(
        request, 'shop/product_list.html', {
            'item': Product.objects.all()
        }
    )

def product(request, pk):
    return render(
        request, 'shop/product_detail.html', {
            'item': Product.objects.get(id=pk)
        }
    )

