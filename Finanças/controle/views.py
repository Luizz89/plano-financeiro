from django.shortcuts import render, redirect
from .models import Gasto

def home(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')

        Gasto.objects.create(
            valor=valor,
            descricao=descricao
        )
        return redirect('home')
    gastos = Gasto.objects.all()
    total = sum(g.valor for g in gastos)
    return render(request,'home.html',{
        'gastos':gastos,
        'total':total
    })
