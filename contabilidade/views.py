from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from vendedoras.models import Maleta, Produtos
from contabilidade.models import Venda

def salvar_vendas(request):
    if request.method == 'POST':
        maleta_id = request.POST.get('maleta_id')
        produto_ids = request.POST.getlist('produtos_selecionados')
        print(produto_ids)

        maleta = get_object_or_404(Maleta, id=maleta_id)
        produtos = Produtos.objects.filter(id__in=produto_ids)

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
    