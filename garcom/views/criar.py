from django.http import HttpResponse
from django.template import loader
from ..models import Garcom
from django.shortcuts import redirect

def criar_garcom(request):
    if request.method == 'POST':
        form = request.POST
        
        nome_completo = form['nome_completo']
        sexo = form['sexo']
        data_nascimento = form['data_nascimento']
        cpf = form['cpf']
        
        try:
            Garcom(nome_completo=nome_completo, 
            sexo=sexo,
            data_nascimento=data_nascimento,
            cpf=cpf
            ).save()
        except:
            return HttpResponse("Deu erro")
        finally:
            return redirect("/garcom?garcom_criado=true")

    elif request.method == "GET":
        template = loader.get_template("criar_garcom.html")
        return HttpResponse(template.render(request=request))