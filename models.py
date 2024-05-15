from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(
      max_length=100,
      null=False,
      blank=False
    )
    sobrenome = models.CharField(
      max_length=100,
      null=False,
      blank=False
    )
    cpf = models.CharField(
      max_length=14 # CPF no formato xxx.xxx.xxx-xx
      null=False,
      blank=False
    )  
    tempo_servico = models.IntegerField(
      default=0,
      null=False,
      blank=False
    )  # Você pode alterar esse campo dependendo de como deseja representar o tempo de serviço
    cargo = models.CharField(
      max_length=100
    )
    remuneracao = models.DecimalField(
      max_digits=10, 
      decimal_places=2,
    )  # Representando a remuneração como um valor decimal

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
