from django.shortcuts import render

def salvar_vendas(request):
    if request.method == "POST":
        selecionados_ids = request.POST.getlist("selecionados")
        itens = Item.objects.filter(id__in=selecionados_ids)

        for item in itens:
            Venda.objects.create(
                tipo=item.tipo,
                valor=item.valor,
                origem=item  # se quiser manter referência ao item original
            )
        return redirect('pagina_de_sucesso')
    