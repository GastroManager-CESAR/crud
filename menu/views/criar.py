from django.http import HttpResponse
from django.template import loader
from ..models import Item
from django.shortcuts import redirect
def criar_item(request):
    if request.method == 'POST':
        form = request.POST
        
        titulo = form['titulo']
        descricao = form['descricao']
        
        try:
            Item(titulo=titulo, descricao=descricao).save()
        except:
            return HttpResponse("Deu erro")
        finally:
            return redirect("/menu?item_criado=true")

    elif request.method == "GET":
        template = loader.get_template("criar.html")
        return HttpResponse(template.render(request=request))