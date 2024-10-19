from django.shortcuts import render, redirect
from .forms import ColaboradorForm, ProdutoForm, EmprestimoForm
from .models import Colaborador, Produto, Emprestimo

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
def relatorioColaboradores(request):
    if(request.method == 'GET'):
        colaboradores = Colaborador.objects.all()
        equipamentos = Produto.objects.all()
        emprestimos = Emprestimo.objects.all()
        
        # colaborador, data de emprestimo, equipamento
        lista = []
        for emprestimo in emprestimos:
            lista.append({
                'colaborador': emprestimo.colaborador.nome,
                'data_emprestimo': emprestimo.data_emprestimo.strftime('%Y-%m-%d'),
                'produto': emprestimo.produto.nome
            })
            
        return render(request, "colaboradores/relatorio.html", {'lista': lista})

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
    produto = Produto.objects.get(id=id)
    produto.delete(keep_parents=False)
    return redirect('lista_produtos')

def cadastrarEmprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, "emprestimos/cadastrar.html", {'form': form})

def listarEmprestimos(request):
    emprestimos = Emprestimo.objects.all()
    json = []
    for emprestimo in emprestimos:
        json.append({
            'colaborador': emprestimo.colaborador.nome,
            'produto': emprestimo.produto.nome,
            'data_emprestimo': emprestimo.data_emprestimo.strftime('%Y-%m-%d'),
            'data_devolucao': emprestimo.data_devolucao.strftime('%Y-%m-%d'),
            'status': emprestimo.status,
            'condicoesEPI': emprestimo.condicoesEPI,
            'motivo_devolucao': emprestimo.motivo_devolucao.__str__(),
            'usuario': emprestimo.usuario.nome
        })
    emprestimos_json = json
    
    return render(request, "emprestimos/listar.html", {'emprestimos': emprestimos, 'json': emprestimos_json})

def editarEmprestimo(request, id):
    emprestimo = Emprestimo.objects.get(id=id)
    form = EmprestimoForm(request.POST or None, instance=emprestimo)
    if form.is_valid():
        form.save()
        return redirect('lista_emprestimos')
    else:
        return render(request, "emprestimos/cadastrar.html", {'form': form})

def removerEmprestimo(request, id):
    if request.method == 'POST':
        emprestimo = Emprestimo.objects.get(id=id)
        emprestimo.delete()
    return redirect('lista_emprestimos')

