from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from profiles.models import Profile
from .forms import ReportForm
from .utils import is_ajax, get_report_image
from .models import Report
from django.views.generic import ListView, DetailView, TemplateView

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

class ReportListView(ListView):
    model = Report
    template_name = "reports/main.html"

class ReportDetailView(DetailView):
    model = Report
    template_name = "reports/detail.html"

class UploadTemplateView(TemplateView):
    template_name = "reports/from_file.html"

def csv_upload_view(request):
    return HttpResponse()

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


def render_pdf_view(request,pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report,pk=pk)
    context = {
        'obj': obj
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if download  use this
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #else if display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

        