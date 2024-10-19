from django.contrib import admin
from .models import Cargo, ListaProduto, Produto, Usuario, Colaborador, Emprestimo

admin.site.register(Cargo)
admin.site.register(ListaProduto)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Colaborador)
admin.site.register(Emprestimo)