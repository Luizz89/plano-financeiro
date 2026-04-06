import json
from urllib import request
from collections import defaultdict
from django.shortcuts import render, redirect
from .models import Gasto
from datetime import date

def home(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao') 

        Gasto.objects.create(
            valor=valor,
            descricao=descricao
        )
        return redirect('home')
    hoje = date.today()
    gastos = Gasto.objects.filter(
        data__day=hoje.day,
        data__month=hoje.month,
    )
    total = sum(g.valor for g in gastos)

    dados = defaultdict(float)
    for g in gastos:
        dados[g.descricao] += float(g.valor)
        
        labels = list(dados.keys())
        valores = list(dados.values())

    return render(request, 'home.html', {
        'gastos': gastos,
        'total': total,
        'labels': json.dumps(labels),
        'valores': json.dumps(valores),
    })


    
