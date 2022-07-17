from django.contrib import admin
from django.urls import path, include
from manejador_contenido.views import mostrar_home, mostrar_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', mostrar_home ),
    path('profile/', mostrar_profile ),
    path('', include('mi_app.urls')),
]
