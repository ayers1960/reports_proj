from django.shortcuts import render
from django.http import JsonResponse
from profiles.models import Profile
from .forms import ReportForm
from .utils import is_ajax, get_report_image
from .models import Report
from django.views.generic import ListView, DetailView

# Create your views here.

class ReportListView(ListView):
    model = Report
    template_name = "reports/main.html"

class ReportDetailView(DetailView):
    model = Report
    template_name = "reports/detail.html"

def create_report_view(request):
    form = ReportForm(request.POST or None)
    if is_ajax(request):
        # name    = request.POST.get('name')
        # remarks = request.POST.get('remarks')
        # image   = request.POST.get('image')
        # author  = Profile.objects.get(user=request.user)
        # img     = get_report_image(image)
        # Report.objects.create(
        #     name=name, 
        #     remarks=remarks,
        #     image=img,
        #     author=author,
        # )
        author  = Profile.objects.get(user=request.user)        
        image   = request.POST.get('image')
        img     = get_report_image(image)  
        if form.is_valid:
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()
            return JsonResponse({'msg': 'send'})
    return JsonResponse({})

        