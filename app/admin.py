from django.contrib import admin
from .models import Cargo, EPIGenerico, ListaEPIGenerico, Produto, Usuario, Colaborador, Emprestimo

admin.site.register(Cargo)
admin.site.register(EPIGenerico)
admin.site.register(ListaEPIGenerico)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Colaborador)
admin.site.register(Emprestimo)