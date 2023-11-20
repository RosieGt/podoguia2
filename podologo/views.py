from django.shortcuts import render
from .models import Podologo
from django.core.paginator import Paginator
from .serializers import PodologoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

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

def cadastrar(request):
    return render(request, "admin/")

def listarpodog(request):
    search = request.GET.get('search')
    
    filter = request.GET.get('filter')
    
   
    if search:
        
        podologo = Podologo.objects.filter(nome__icontains=search)
    
    elif filter:
        podologo = Podologo.objects.filter(done=filter)
        
    else:
        podologo_list = Podologo.objects.all()
    
        paginator = Paginator(podologo_list, 10)
    
        page = request.GET.get('page')
    
        podologo = paginator.get_page(page)
      
    return render(request, 'listapodog.html', 
                  {'podologo' : podologo })


class PodologoViewSet(ReadOnlyModelViewSet):
    queryset = Podologo.objects.all()
    serializer_class = PodologoSerializer 
    filter_backends = [filters.SearchFilter]
    search_fields = ["nome"]