from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html', {'title': 'Cadastrar'})

def usuarios(request):
    
    usuarios= {
        'usuarios': Usuario.objects.all(),
        'title': 'Usuários'
        
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def salvar(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    return redirect('listagem_usuarios')
    
def editar(request, id):
    usuario = Usuario.objects.get(id_user=id)
    return render(request, 'ajustes/atualizar.html',{'usuario': usuario})

def atualizar(request, id):
    novo_nome = request.POST.get('nome')
    nova_idade = request.POST.get('idade')
    usuario = Usuario.objects.get(id_user=id)
    usuario.nome = novo_nome
    usuario.idade = nova_idade
    usuario.save()
    return redirect('listagem_usuarios')
    

def deletar(request, id):
    usuario = Usuario.objects.get(id_user=id)
    usuario.delete()
    return redirect('listagem_usuarios')
    

    