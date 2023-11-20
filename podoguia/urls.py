"""
URL configuration for podoguia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from podologo.views import index_copy, home, listarpodog, cadastrar,  detalhar,  PodologoViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register("podoguia", PodologoViewSet, basename="podoguia")

urlpatterns = [
    path('index_copy/', index_copy, name="index_copy"),
    path('', home, name="home"),
    path('listarpodog/', listarpodog, name='listarpodog'),
    path('admin/', admin.site.urls),
    path('detalhar/<int:id>', detalhar, name="detalhar"),
    path('api/', include(routers.urls)),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
