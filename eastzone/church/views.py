from django.shortcuts import render
from . models import Church

# Create your views here.
def church(request):
    churchs = Church.objects.all()
    return render(request, "church/church.html", {'churchs':churchs})