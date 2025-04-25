from django.shortcuts import get_object_or_404, redirect
from vendedoras.models import Maleta, Produto
from contabilidade.models import Venda

def salvar_vendas(request):
    if request.method == 'POST':
        maleta_id = request.POST.get('maleta_id')
        produto_ids = request.POST.getlist('produtos_selecionados')

        maleta = get_object_or_404(Maleta, id=maleta_id)
        produtos = Produto.objects.filter(id__in=produto_ids)

        for produto in produtos:
            Venda.objects.create(
                maleta=maleta,
                produto=produto,
                valor=produto.valor
            )

        return redirect('pagina_de_sucesso')
    