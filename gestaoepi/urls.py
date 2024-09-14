"""
URL configuration for gestaoepi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),  # Exemplo de path para uma view específica
    path('colaborador/cadastrar', views.cadastrarColaborador, name='cadastro_colaborador'),
    path('colaboradores/', views.listarColaboradores, name='lista_colaboradores'),
    path('colaborador/<int:id>/editar', views.editarColaborador, name='editar_colaborador'),
    path('colaborador/<int:id>/remover', views.removerColaborador, name='remover_colaborador'),
    path('epi/cadastrar', views.cadastrarEPI, name='cadastro_epi'),
    path('epis/', views.listarEPIs, name='lista_epis'),
    path('epi/<int:id>/editar', views.editarEPI, name='editar_epi'),
    path('epi/<int:id>/remover', views.removerEPI, name='remover_epi'),
]
