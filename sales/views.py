from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm

# Create your views here.

def home_view(request):
    sales_df = None
    positions_df = None

    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to   = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(f"{date_from} => {date_to}  {chart_type}")
        sale_qs = Sale.objects.filter(created__date__lte=date_to,
                                 created__date__gte=date_from
                                 )
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())
            positions_data = []
            for sale in sale_qs:
                print(f"sale:{sale}")
                for pos in sale.get_positions():
                    obj = {
                        'position_id' : pos.id,
                        'product'     : pos.product.name,
                        'quantity'    : pos.quantity,
                        'price'       : pos.price
                    }
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data).to_html()

            sales_df = sales_df.to_html()
        else:
            print('no data')

    
    context = {
        'form' : form,
        'sales_df': sales_df,
        'positions_df': positions_df,
    }
    return render(request, 'sales/home.html', context)

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