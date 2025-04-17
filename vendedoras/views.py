from django.shortcuts import render,redirect
from vendedoras.forms import RepresentantesModelForm
# Create your views here.

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