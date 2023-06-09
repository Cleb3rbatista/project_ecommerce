from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
import re
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .models import usuarios



# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def cadastro(request):
    if request.method != 'POST':
        return render(request,'cadastro.html',{})

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    confirmaemail = request.POST.get('confirmaemail')
    telefone = request.POST.get('telefone')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    confirmasenha = request.POST.get('confirmasenha')
    data_nascimento = request.POST.get('nascimento')
        
    # Valida se o campo nome esta vazio 
    if not nome:
        messages.error(request,"O campo nome deve ser preenchido")
        return render(request, 'cadastro.html')
    
    # Valida se o campo nome tem caracteres especiais ou numeros
    padrao = r'^[a-zA-Z\sÀ-ÖØ-öø-ÿ]*$'
    if not re.match(padrao, nome):
        messages.error(request,"O campo nome não de conter numeros ou caracteres especias")
        return render(request, 'cadastro.html')
    
    # Valida se o campo nome tem mais de 3 caracteres
    if len(nome) <= 3: 
        messages.error(request,"O campo nome deve conter no minimo 3 caracteres")
        return render(request, 'cadastro.html')
    
    # valida se o campo sobrenome esta vazio
    if not sobrenome:
        messages.error(request,"O campo sobrenome deve ser preenchido")
        return render(request, 'cadastro.html')
    
    # valida se o campo sobrenome tem caracteres especiais ou numeros
    padrao = r'^[a-zA-Z\sÀ-ÖØ-öø-ÿ]*$'
    if not re.match(padrao, sobrenome):
        messages.error(request,"O campo nome não de conter numeros ou caracteres especias")
        return render(request, 'cadastro.html')
    
    # Valida se o campo sobrenome tem mais de 3 caracteres
    if len(sobrenome) <= 3: 
        messages.error(request,"O campo sobrenome deve conter no minimo 3 caracteres")
        return render(request, 'cadastro.html')
    
    # Valida se o campo cpf tem todos os caracteres
    if len(cpf) != 14:
        messages.error(request,"O campo cpf deve conter 11 caracteres")
        return render(request, 'cadastro.html')
    
    # Valida se o cpf tem todos os numeros iguais
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf == cpf[0] * 11:
        messages.error(request,"CPF invalido")
        return render(request, 'cadastro.html')
    
    # Valida se o primeiro digito verificador e valido
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[9]) != resto:
        messages.error(request,"CPF invalido")
        return render(request, 'cadastro.html')
        
    # Valida se o segundo digito verificador e valido
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if int(cpf[10]) != resto:
        messages.error(request,"CPF invalido")
        return render(request, 'cadastro.html')
    
    # Valida se o email foi digitado
    if not email:
        messages.error(request,"O campo email deve ser preenchido")
        return render(request, 'cadastro.html')       
    
    # Valida email
    try:
        validate_email(email)
    except:
        messages.error(request,"email invalido. Ex.: email@example.com")
        return render(request, 'cadastro.html')
    
    #Valida se o email já esta cadastrado
    if User.objects.filter(email=email).exists():
        messages.error(request,"Email já cadastrado")
        return render(request, 'cadastro.html')
    
    # Valida se os campos de email estão iguais
    if email != confirmaemail:
        messages.error(request,"E-mails diferentes, verifique")
        return render(request, 'cadastro.html')       
        
      # Valida se o campo telefone esta vazio  
    if not telefone:
        messages.error(request,"O campo telefone deve ser preenchido")
        return render(request, 'cadastro.html')      

    # Valida se o campo telefone tem 11 numeros
    if len(telefone) != 15:
        messages.error(request,"O campo telefone deve ter 11 numeros")
        return render(request, 'cadastro.html')   
        
    # Valida se o campo usuario ja esta cadastrado
    if User.objects.filter(username=usuario).exists():
        messages.error(request,"Usuario já cadastrado")
        return render(request, 'cadastro.html')
    
    # Valida se o campo usuario tem 5 ou menos caracteres 
    if len(usuario) <= 5:
        messages.error(request,"Usuario deve ter no minimo 6 caracteres")
        return render(request, 'cadastro.html')
    
    # Valida se senha esta vazia
    if not senha:
        messages.error(request,"O campo senha deve ser preenchido")
        return render(request, 'cadastro.html')      
    
    # Valida se o campo senha tem menos de 6 caracteres
    if len(senha) <= 5:
        messages.error(request,"Senha deve ter no minimo 6 caracteres")
        return render(request, 'cadastro.html')
    
    # Valida se o campo senha tem numeros, letra e caracteres especias
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$'
    if not re.match(padrao, senha):
        messages.error(request,"A senha deve conter letras maiusculas, letras minusculas, numeros e caracteres especias")
        return render(request, 'cadastro.html')
    
    # Valida se as senhas digitas são iguas
    if senha != confirmasenha:
        messages.error(request,"Senhas devem ser iguais")
        return render(request, 'cadastro.html')
    
    # Valida se o campo data_nascimento esta vazio
    if  not data_nascimento:
        messages.error(request,"O campo data de nascimento deve ser preenchido")
        return render(request, 'cadastro.html')             

    messages.success(request, "Usuario cadastrado com sucesso !")

    user = User.objects.create_user(username=usuario,
                                                      password=senha,
                                                      email = email,
                                                      first_name = nome,
                                                      last_name = sobrenome)
    user.save()

    Cadusuarios =usuarios(
        nome=nome,
        sobrenome=sobrenome,
        email=email,
        usuario = usuario,
        cpf = cpf,
        telefone = telefone,
        data_nascimento=data_nascimento,
        id_User = user
    )
    Cadusuarios.save()
    
    
    return render(request, 'cadastro.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request,username=username, password=password)
        if  user is not None:
            login(request,user)
            return redirect('pesquisaprodutos')
        else:
            messages.error(request, 'usuario ou senha invalido')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def pesquisaprodutos(request):
    produtos = range(6)
    return render(request, 'pesquisaprodutos.html',{'produtos':produtos})