from django.db import models

AVALIACAO = (
    (0, 'Ótimo'),
    (1, 'Bom'),
    (2, 'Regular'),
    (3, 'Ruim'),
    (4, 'Péssimo'),
)


class Hospede(models.Model):
    nome = models.CharField(max_length=120, verbose_name='Nome')
    cpf = models.CharField(unique=True, max_length=20, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=120, verbose_name='Endereço')
    avaliacao = models.IntegerField(choices=AVALIACAO, blank=True, null=True, verbose_name='Avaliação')
    observacao = models.TextField(verbose_name='Observações', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Hóspedes'
        verbose_name = 'Hóspede'
