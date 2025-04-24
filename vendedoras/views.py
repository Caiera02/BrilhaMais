from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from vendedoras.forms import RepresentantesModelForm
from vendedoras.models import Maleta
# Create your views here.

@login_required(login_url='/admin/')
def cadastro_view(request):
    if request.method =='POST':
        new_form= RepresentantesModelForm(request.POST)
        print(new_form.data)
        if new_form.is_valid():
            new_form.save()
            return redirect('new_cadastro')
    else:
        new_form= RepresentantesModelForm()
    return render( 
    request,
    'cadastro.html',
    {'new_form': new_form}
)
    
def maleta_view(request):
    maletas=Maleta.objects.all()
    paginator =Paginator(maletas,1)
    page_number = request.GET.get('page')
    maleta = paginator.get_page(page_number)
    return render(request,
                  'romaneio.html',
                  {'maleta':maleta})