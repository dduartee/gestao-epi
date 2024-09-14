from django.shortcuts import render, redirect
from .forms import ColaboradorForm, EPIForm
from .models import Colaborador, EPIGenerico

# Create your views here.

def home(request):
    return render(request, "index.html")

def cadastrarColaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_colaboradores')
    else:
        form = ColaboradorForm()
    return render(request, "colaboradores/cadastrar.html", {'form': form})

def listarColaboradores(request):
    if(request.method == 'GET'):
        colaboradores = Colaborador.objects.all()
        return render(request, "colaboradores/listar.html", {'colaboradores': colaboradores})

def editarColaborador(request, id):
    colaborador = Colaborador.objects.get(id=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)
    if form.is_valid():
        form.save()
        return redirect('lista_colaboradores')
    else:
        return render(request, "colaboradores/cadastrar.html", {'form': form})

def removerColaborador(request, id):
    if(request.method == 'POST'):
        colaborador = Colaborador.objects.get(id=id)
        colaborador.delete()
    return redirect('lista_colaboradores')

def cadastrarEPI(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_epis')
    else:
        form = EPIForm()
    return render(request, "epis/cadastrar.html", {'form': form})

def listarEPIs(request):
    EPIs = EPIGenerico.objects.all()
    return render(request, "epis/listar.html", {'epis': EPIs})

def editarEPI(request, id):
    epi = EPIGenerico.objects.get(id=id)
    form = EPIForm(request.POST or None, instance=epi)
    if form.is_valid():
        form.save()
        return redirect('lista_epis')
    else:
        return render(request, "epis/cadastrar.html", {'form': form})

def removerEPI(request, id):
    if(request.method == 'POST'):
        epi = EPIGenerico.objects.get(id=id)
        epi.delete()
    return redirect('lista_epis')    