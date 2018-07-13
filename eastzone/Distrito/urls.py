"""Distrito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings

urlpatterns = [    
    #path del core
    path('', include('core.urls')),
    
    #path del church
    path('church/', include('church.urls')),
    
    #path del admin
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'Embajadores de Cristo' #Título primario del panel
admin.site.index_title = 'Panel de administrador' #Título secundatrio del panel
admin.site.site_title = 'Embajadores de Cristo' #Nombre en la pestaña de navegador    
    
    
    
