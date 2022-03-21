from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import EmpresaForm
from django.contrib import messages

from .models import Empresa

def homePrincipal(request):

    search = request.GET.get('search')

    if search:

        empresas = Empresa.objects.filter(nomeEmpresa__icontains=search)

    else :

        empresas_lista = Empresa.objects.all()
        
        paginator = Paginator(empresas_lista, 6)
        page = request.GET.get('page')

        empresas = paginator.get_page(page)

    return render(request, 'empresa/home.html', {'empresa': empresas})


def empresaView(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    return render(request, 'empresa/empresa.html', {'empresa': empresa})


def novaEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.pronto = 'Ativo'
            empresa.save()
            messages.success(request, 'Empresa adicionada com sucesso!')
            return redirect('/')
            

    else:
        form = EmpresaForm()
        return render(request, 'empresa/adicionar-empresa.html', {'form': form})
        


def editarEmpresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(instance=empresa)

    if(request.method == 'POST'):
        form = EmpresaForm(request.POST, instance=empresa)

        if(form.is_valid()):
            empresa.save()
            messages.info(request, 'Empresa foi editada com sucesso!')   
            return redirect('/') 
        else:
            return render(request, 'empresa/editar-empresa.html', {'form': form, 'empresa': empresa})
    else:
        return render(request, 'empresa/editar-empresa.html', {'form': form, 'empresa': empresa})


def removerEmpresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    empresa.delete()

    messages.warning(request, 'Empresa excluida com sucesso!')

    return redirect('/')


