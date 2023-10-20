from django.shortcuts import render
from .models import Podologo
from .serializers import PodologoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your views here.
def index(request):
    podologos = Podologo.objects.all()
    
    return render(request, "index.html", {'podologos': podologos})
def home(request):
    podologos = Podologo.objects.all()
    
    return render(request, "home.html",  {'podologos': podologos})

def detalhar(request, id):
    podologo = podologos = Podologo.objects.get(id=id)
    return render(request, "detalhar.html", {"podologo": podologo})

class PodologoViewSet(ReadOnlyModelViewSet):
    queryset = Podologo.objects.all()
    serializer_class = PodologoSerializer    