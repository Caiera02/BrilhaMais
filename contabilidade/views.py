from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Sum
from decimal import Decimal
from django.core.paginator import Paginator
from django.utils import timezone
import locale
from vendedoras.models import Maleta, Produto, Representantes
from contabilidade.models import Venda

locale.setlocale(locale.LC_TIME,'pt_BR.UTF-8')

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
        total_format = f'{total:,.2f}'.replace(',','.')
        
        if total >=1000:
            porcentagem = Decimal('0.40')
        elif total >=500:
            porcentagem = Decimal('0.30')
        elif total <=499:
            porcentagem= Decimal('0.20')
        else:
            porcentagem = Decimal('0.00')#sem comissão
        
        comissaoVendedora = total * porcentagem
        comissaoVendedora = f'R$ {comissaoVendedora:,.2f}'.replace(",", ".").replace(".", ".").replace("X", ".")
        
        dados.append({
            'maleta': maleta,
            'vendas': vendais,
            'total': total_format,
            'comissaoVendedora':comissaoVendedora,
            'porcentagem': porcentagem
        })
        # print(dados)
      
    paginator = Paginator(dados, 1)
    page_number = request.GET.get('page')
    dados = paginator.get_page(page_number)       
    

    return render(request, 'vendas.html', {'dados': dados , 'vendas':venda},)

def dashboard_view(request):
    hoje =timezone.now()
    mes = hoje.strftime('%B').capitalize()
    
    # Pega o queryset filtrado
    VendaMes = Venda.objects.filter(
        data_venda__year=hoje.year,
        data_venda__month=hoje.month
    )

    # Conta a quantidade de vendas
    quantidade_vendas = VendaMes.count()

    # Soma os valores
    soma_venda_mes = VendaMes.aggregate(soma=Sum('valor'))['soma'] or 0
    comissao = soma_venda_mes * Decimal(0.15)
    comissao_format = f'{comissao:,.2f}'.replace(',','.')
    
    totalVendedora= Representantes.objects.filter(ativo= True).count()
    return render (request, 'dashboard.html',{'total':totalVendedora,'totalVenda':soma_venda_mes,'quantidaVenda':quantidade_vendas,'mes':mes, 'comissao':comissao_format})