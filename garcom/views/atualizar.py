from django.http import HttpResponse
from django.template import loader
from ..models import Garcom

def atualizar_garcom(request, id):
    if request.method == 'POST':
        form = request.POST

        nome_completo = form['nome_completo']
        cpf = form['cpf']
        data_nascimento = form['data_nascimento']
        sexo = form['sexo']
        foto = form['foto']
        
        try:
            Garcom.objects.filter(id=id).update(nome_completo=nome_completo, cpf=cpf, data_nascimento=data_nascimento, sexo=sexo, foto=foto)
        except:
            return HttpResponse("item não encontrado")
        finally:
            return HttpResponse("Sucesso")