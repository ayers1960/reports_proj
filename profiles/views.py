from django.shortcuts import render

# Create your views here.
from .models import Profile
from .forms import ProfileForm

def my_profile_view(request):
    context = {}
    return render(request, 'profiles/main.html', context)