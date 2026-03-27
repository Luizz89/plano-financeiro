from django.shortcuts import render
from .models import Transacao

def home(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')

        Transacao.objects.create(
            valor=valor,
            tipo=tipo,
            descricao=descricao
        )
        return redirect('home')
    trasacoes = Transacao.objects.all()
    saldo = 0
    for t in trasacoes:
        if t.tipo == 'entrada':
            saldo +=t.valor
        else:
            saldo -=t.valor

    return render(request,'home.html',{
        'transacoes':trasacoes,
        'saldo':saldo
    })
