from django.http import HttpResponse
from django.template import loader
from ..models import Item

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
            return HttpResponse("Sucesso")