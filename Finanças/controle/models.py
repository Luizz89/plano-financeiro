from django.db import models

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saida')
    ]
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=100) 
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.valor}"