from django.shortcuts import render
from .models import SiteSettings, Direction


# Create your views here.
def index(request):
    site_settings = SiteSettings.objects.first()
    directions = Direction.objects.all()
    return render(request, 'index.html', {'site_settings': site_settings, 'directions': directions})

def cybersecurity(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'cybersecurity.html', {'site_settings': site_settings})

def cybersport(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'cybersport.html', {'site_settings': site_settings})

def design(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'design.html', {'site_settings': site_settings})

def information_technology(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'information-technology.html', {'site_settings': site_settings})

def movie_and_video(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'movie-and-video.html', {'site_settings': site_settings})

def olimp(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'olimp.html', {'site_settings': site_settings})

def robots(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'robots.html', {'site_settings': site_settings})

def solutions(request):
    site_settings = SiteSettings.objects.first()
    return render(request, 'solutions.html', {'site_settings': site_settings})