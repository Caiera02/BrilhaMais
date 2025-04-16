from django.shortcuts import render

# Create your views here.

def cadastro_view(request):
    return render( 
        request,
        'cadastro.html',
    )