from django.http import HttpResponse
from django.template import loader
from ..models import Garcom
def criar_garcom(request):
    if request.method == 'POST':
        form = request.POST
        
        nome_completo = form['nome_completo']
        sexo = form['sexo']
        data_nascimento = form['data_nascimento']
        foto = form['foto']
        cpf = form['cpf']
        
        try:
            Garcom(nome_completo=nome_completo, 
            sexo=sexo,
            data_nascimento=data_nascimento,
            foto=foto,
            cpf=cpf
            ).save()
        except:
            return HttpResponse("Deu erro")
        finally:
            return HttpResponse("Obrigado por se cadastrar")

    else:
        return HttpResponse("Inválido")