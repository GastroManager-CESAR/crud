from django.http import HttpResponse
from django.template import loader
from ..models import Item
from django.shortcuts import redirect

def atualizar_item(request, id):
    if request.method == 'POST':
        form = request.POST

        titulo = form['titulo']
        descricao = form['descricao']
        
        try:
            Item.objects.filter(id=id).update(titulo=titulo, descricao=descricao)
        except:
            return HttpResponse("item não encontrado")
        finally:
            return redirect("/menu")
    elif request.method == "GET":
        template = loader.get_template("atualizar.html")
        context= {
            "id": id
        }
        return HttpResponse(template.render(request=request, context=context))