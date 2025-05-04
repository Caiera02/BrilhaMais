from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Sum
from vendedoras.models import Maleta, Produto
from contabilidade.models import Venda

def salvar_vendas(request):
    if request.method == 'POST':
        maleta_id = request.POST.get('maleta_id')
        produto_ids = request.POST.getlist('produtos_selecionados')
        print(produto_ids)

        maleta = get_object_or_404(Maleta, id=maleta_id)
        produtos = Produto.objects.filter(id__in=produto_ids)

        for produto in produtos:
            Venda.objects.create(
                maleta=maleta,
                produto=produto,
                valor=produto.valor
            )
        messages.success(request, 'Venda realizada com sucesso!')
        return redirect('produto_list')

    # se não for POST (por exemplo, GET), redireciona ou mostra página de erro
    messages.warning(request, 'Acesso inválido.')
    return redirect('vendas_list')  # ou redireciona para uma página segura

def vendas_view(request):
    maletas = Maleta.objects.all()
    venda = Venda.objects.all()

    dados = []
    for maleta in maletas:
        vendais = Venda.objects.filter(maleta=maleta).select_related('produto')
        total = vendais.aggregate(total=Sum('valor'))['total'] or 0
        dados.append({
            'maleta': maleta,
            'vendas': dados,
            'total': total
        })

    return render(request, 'vendas.html', {'dados': dados , 'vendas':venda})
