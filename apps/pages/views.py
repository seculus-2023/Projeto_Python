from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Projeto, Contato , MembroEquipe


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        if nome and email and mensagem:
            contato = Contato.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                mensagem=mensagem
            )
            # Envia e-mail para endereço fixo
            send_mail(
                subject=f'Novo contato de {nome}',
                message=f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['arpjunior40@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
        else:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
    return render(request, 'contato.html')

def equipe(request):
    return render(request, 'equipe.html')

def projetos(request):
    projetos = Projeto.objects.filter(ativo=True)
    return render(request, 'projetos.html', {'projetos': projetos})

def politica(request):
    return render(request, 'politica.html')

def membros(request):
    membros = MembroEquipe.objects.all()
    return render(request, 'membros.html', {'equipe': membros})