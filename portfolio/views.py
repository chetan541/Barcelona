from django.shortcuts import render
from .models import member



# Create your views here.
def home(request):
    barca=member.objects.all().order_by('title')
    projects=member.objects.filter().values()
    return render(request,'portfolio/home.html',{'barca':barca})

