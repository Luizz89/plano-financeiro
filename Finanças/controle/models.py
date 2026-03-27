from django.db import models

class Gasto(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    descricao = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.valor}"