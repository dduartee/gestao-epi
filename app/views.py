from django.shortcuts import render, redirect
from .forms import ColaboradorForm, EPIForm, ProdutoForm
from .models import Colaborador, EPIGenerico, Produto

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

def cadastrarProdutos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, "produtos/cadastrar.html", {'form': form})

def listarProdutos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/listar.html", {'produtos': produtos})

def editarProdutos(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    else:
        return render(request, "produtos/cadastrar.html", {'form': form})
    
def removerProdutos(request, id):
    if(request.method == 'POST'):
        produto = Produto.objects.get(id=id)
        produto.delete()
    return redirect('lista_produtos')


