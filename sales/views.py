from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Sale

# Create your views here.

def home_view(request):
    hello = 'hello world from the view'
    return render(request, 'sales/home.html', {'h':hello})

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'    

def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request, 'sales/main.html', {'object_list':qs})

def sale_detail_view(request, pk):
    obj = Sale.objects.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk )
    return render(request, 'sales/detail.html', {'object':obj})
'''
 in the urls
 path('sales/', sale_list_view, name='list')
 path('sales/<pk>/', sale_detail_view, name='detail')
'''