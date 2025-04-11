from django.db import models
from django.core.validators import RegexValidator

class BichosEstimacao(models.Model):
    nome = models.CharField(max_length=20)
    opcoes_racas = [
        ('Coruja', 'Coruja'),
        ('Gato', 'Gato'),
        ('Leao', 'Leão'),
        ('Rato', 'Rato')
    ]
    raca = models.CharField(max_length=20, choices=opcoes_racas)

    def __str__(self):
        return self.nome

class PersonagemHarryPotter(models.Model):
    nome = models.CharField(max_length=50)
    escolha_casas = [
        ('Grifinoria', 'Grifinória'),
        ('Lufa-Lufa', 'Lufa-Lufa'),
        ('Corvinal', 'Corvinal'),
        ('Sonserina', 'Sonserina')
    ]
    casa = models.CharField(max_length=25, choices=escolha_casas)
    validador_cpf = RegexValidator (
        regex=r'^\d{3}.\d{3}.\d{3}-\d{2}$',
        message='O CPF do bruxo deve estar no formato XXX.XXX.XXX-XX'
    )
    cpf = models.CharField(max_length=14, unique=True, validators=[validador_cpf])
    qnt_de_nariz = models.IntegerField(blank=True, null=True)
    status = models.BooleanField()
    patrono = models.CharField(max_length=50, blank=True, null=True)
    animal = models.ForeignKey('BichosEstimacao', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome