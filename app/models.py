from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    prazo_dias = models.IntegerField()
    qtd_estoque = models.IntegerField()
    numero_ca = models.CharField(max_length=255)
    data_validade_ca = models.DateField()

    def __str__(self):
        return f'{self.nome} - CA: {self.numero_ca}'

class ListaProduto(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cargo.nome} - {self.epi_generico.nome}'

class Usuario(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    statuschoice = (
        ('Emprestado', 'Emprestado'),
        ('Em uso', 'Em uso'),
        ('Forneceido', 'Fornecido'),
        ('Devolvido', 'Devolvido'),
        ('Danificado', 'Danificado'),
        ('Perdido', 'Perdido'),
    )
    condicoesEPI = (
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Ruim', 'Ruim')
    )
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.TextField(choices=statuschoice)
    condicoesEPI = models.TextField(choices=condicoesEPI)
    motivo_devolucao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Emprestimo de {self.produto.nome} para {self.colaborador.nome}'
