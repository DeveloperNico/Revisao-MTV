from django.shortcuts import render, redirect, get_object_or_404
from .models import BichosEstimacao, PersonagemHarryPotter
from .forms import PersonagemForm

def listar_personagens(request):
    personagens = PersonagemHarryPotter.objects.all()
    return render(request, 'listagem.html', {'personagens': personagens})

def criar_bruxo(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
    return render(request, 'formulario.html', {'formulario': form})

def atualizar_bruxo(request, pk):
    personagem = get_object_or_404(PersonagemHarryPotter, pk=pk)
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm(instance=personagem)
    return render(request, 'formulario.html', {'formulario': form})

def deletar_bruxo(request, pk):
    personagem = get_object_or_404(PersonagemHarryPotter, pk=pk)
    if request.method == 'POST':
        personagem.delete()
        return redirect('listar_personagens')
    return render(request, 'confirmar_delete.html', {'personagem': personagem})