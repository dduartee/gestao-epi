from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class EPIGenerico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    prazo_dias = models.IntegerField()

    def __str__(self):
        return self.nome


class ListaEPIGenerico(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    epi_generico = models.ForeignKey(EPIGenerico, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cargo.nome} - {self.epi_generico.nome}'


class Produto(models.Model):
    epi_generico = models.ForeignKey(EPIGenerico, on_delete=models.CASCADE)
    qtd_estoque = models.IntegerField()
    numero_ca = models.CharField(max_length=255)
    data_validade_ca = models.DateField()

    def __str__(self):
        return f'{self.epi_generico.nome} - CA: {self.numero_ca}'


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
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    prazo_uso = models.IntegerField()
    motivo_devolucao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Emprestimo de {self.produto.epi_generico.nome} para {self.colaborador.nome}'
