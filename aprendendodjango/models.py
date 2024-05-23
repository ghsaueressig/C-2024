from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    chefia = models.BooleanField(
        default=False
    )

    biografia = models.CharField(
        default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus et arcu turpis. Nunc sit amet elit tempus justo semper mattis et eget nisl. Cras vitae sapien vulputate dui faucibus interdum sed in justo. Nam in pharetra risus. Duis pellentesque tellus.',
        max_length=255,
        blank=False
    )
    
    def __str__(self):
        return self.nome + " " + self.sobrenome

    objetos = models.Manager()

class Equipe(models.Model):
    nome = models.CharField(
        max_length=255,
        unique=True
    )
    integrantes = models.ManyToManyField(
        Funcionario,
        related_name='equipe'
    )
    descricao = models.CharField(
        default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus et arcu turpis. Nunc sit amet elit tempus justo semper mattis et eget nisl. Cras vitae sapien vulputate dui faucibus interdum sed in justo. Nam in pharetra risus. Duis pellentesque tellus.',
        max_length=255,
        blank=False
    )
    def __str__(self):
        return self.nome

    objetos = models.Manager()

    # query para retornar funcionarios de uma equipe
    # Equipe.objects.get(id=1)
    # funcionarios = equipe.funcionarios.all()
    # # OTIMIZANDO
    # equipe = Equipe.objects.prefetch.related('funcionarios').get(id=1).filter(id=1).first()

class Tarefa(models.Model):
    STATUS_CHOICES = (
        ("1","ABERTO"),
        ("2","EM ANDAMENTO"),
        ("3","FECHADO"),
    )
    nome = models.CharField(
        max_length=255,
        unique=True
    )
    equipe=models.ForeignKey(
        Equipe,
        null=False,
        related_name='tarefa',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='1',
        max_length=255
    )
    descricao = models.CharField(
        default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus et arcu turpis. Nunc sit amet elit tempus justo semper mattis et eget nisl. Cras vitae sapien vulputate dui faucibus interdum sed in justo. Nam in pharetra risus. Duis pellentesque tellus.',
        max_length=255,
        blank=False
    )
    def __str__(self):
        return self.nome