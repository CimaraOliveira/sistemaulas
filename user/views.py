from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login as ts_login
from setuptools.extension import Library

from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sqlparse.sql import For

from disciplina.models import Disciplina,Usuario, UsuarioDisciplina
from django.http import HttpResponseRedirect, HttpResponse
from .models import FormDadosUsu, FormUsuDisc


from django.views import View



#@login_required(redirect_field_name='login')
class HomeUsuario(ListView):
    model = Disciplina
    template_name = 'disciplina/home.html'

    context_object_name = 'disciplinas'


class DetalhesDisciplina(DetailView):
    model = Disciplina
    template_name = 'user/detail.html'
    context_object_name = 'disciplina'
    slug_url_kwarg = 'slug'

def criar(request):
    if request.method != 'POST':
        return render(request, 'user/criar.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    user_choice = request.POST.get('user_choice')

    if not nome or not email or not usuario or not senha \
            or not user_choice or not senha2:
        messages.error(request, 'Preencha todos os Campos!')
        return render(request, 'user/criar.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email Inválido!')
        return render(request, 'user/criar.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter pelo menos 6 Caracteres!')
        return render(request, 'user/criar.html')

    if senha != senha2:
        messages.error(request, 'Senhas não Conferem!')
        return render(request, 'user/criar.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'user/criar.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Esse nome de Usuário já existe!')
        return render(request, 'user/criar.html')

    messages.success(request, 'Usuário Registrado com Sucesso!')

    user = User.objects.create_user(email=email, username=usuario,  password=senha,
                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('user:login')
    #return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')
        #return redirect('login')

    if request.method != 'POST':
        return render(request, 'user/login.html')
        #return redirect('login')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    if not usuario or not senha:
        messages.error(request, 'Preencha os campos!')
        return redirect('user:login')

        #return redirect('login')

    user = auth.authenticate(request, username=usuario, password=senha)

    if user is not None:
        if user.usuario.professor:
            messages.success(request, 'Login efetuado com Sucesso!')
            return redirect('professor:detail')

        else:
            messages.success(request, 'Login efetuado com Sucesso!')
            return redirect('disciplina:listar')



         #messages.success(request, 'Login efetuado com Sucesso!')
            #return redirect('disciplina:listar')
    messages.error(request, 'Usuário ou Senha Inválidos!')
    return redirect('user:login')
    # return redirect('login')

def index(request):
    return render(request,'user/index.html')

def reservarDisciplina(request):
    form = FormUsuDisc(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('user:reservarDisciplina')
    else:
        form = FormUsuDisc(request.POST, request.FILES)

    context = {
        'form': form
    }

    return render(request, 'user/reservarDisciplina.html', context)



def editarUsuario(request,id):
      data = {}
      usuario = Usuario.objects.get(id=id)
      form = FormDadosUsu(request.POST or None, instance=usuario)

      if form.is_valid():
        form.save()
        return redirect('user:editarUsuario')

      data['form'] = form
      data['usuario'] = usuario

      return render(request, 'user/editarUsuario.html', data)


"""def detalhesUsuario(request,id):
   form = get_object_or_404(Usuario, id=id)
   if request.method == 'POST':
       form = FormDadosUsu(request.POST, instance=form)
       if form.is_valid():
           form =form.save()
           messages.success(request, 'Sucess update')
       else:
           messages.error(request, 'Erro')

       form = Usuario(isinstance=form)
   return render(request, 'user/detalhesUsuario.html', {'form':form})"""


#@login_required()
def user_logout(request):
    logout(request)
    return redirect('user:login')

def alterarSenha(request):
    pass



def minhasDisciplinas(request):

    usuariodisciplinas = UsuarioDisciplina.objects.filter(usuario_id = request.user.id)
    context ={
        'usuariodisciplinas' : usuariodisciplinas
    }
    print(usuariodisciplinas)
    return render(request, 'user/minhasDisciplinas.html', context)


def listarPedidosReserva(request):
 pass


