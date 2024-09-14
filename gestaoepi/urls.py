from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Gerenciamento de colaboradores
    path('colaborador/cadastrar', views.cadastrarColaborador, name='cadastro_colaborador'),
    path('colaboradores/', views.listarColaboradores, name='lista_colaboradores'),
    path('colaborador/<int:id>/editar', views.editarColaborador, name='editar_colaborador'),
    path('colaborador/<int:id>/remover', views.removerColaborador, name='remover_colaborador'),

    # Gerenciamento de EPIs
    path('epi/cadastrar', views.cadastrarEPI, name='cadastro_epi'),
    path('epis/', views.listarEPIs, name='lista_epis'),
    path('epi/<int:id>/editar', views.editarEPI, name='editar_epi'),
    path('epi/<int:id>/remover', views.removerEPI, name='remover_epi'),

    # Gerenciamento de Produtos
    path('produto/cadastrar', views.cadastrarProdutos, name='cadastro_produto'),
    path('produtos/', views.listarProdutos, name='lista_produtos'),
    path('produto/<int:id>/editar', views.editarProdutos, name='editar_produto'),
    path('produto/<int:id>/remover', views.removerProdutos, name='remover_produto'),

    # Gerenciamento de Empréstimos
    path('emprestimo/cadastrar', views.cadastrarEmprestimo, name='cadastro_emprestimo'),
    path('emprestimos/', views.listarEmprestimos, name='lista_emprestimos'),
    path('emprestimo/<int:id>/editar', views.editarEmprestimo, name='editar_emprestimo'),
    path('emprestimo/<int:id>/remover', views.removerEmprestimo, name='remover_emprestimo'),
]
