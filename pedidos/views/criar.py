from django.http import HttpResponse
from django.template import loader
from ..models import Pedido
from garcom.models import Garcom
from menu.models import Item
from django.shortcuts import redirect

def criar_pedido(request):
    if request.method == 'POST':
        form = request.POST
        
        item = form['item']
        preco = form['preco']
        mesa = form['mesa']
        garcom = form['garcom']
        descricao = form['descricao']
        
        try:
            Pedido(item=item, preco=preco, mesa=mesa, garcom=garcom, descricao=descricao).save()
        except:
            return HttpResponse("Deu erro")
        finally:
            return redirect("/pedidos?pedido_criado=true")

    elif request.method == "GET":
        lista_garcons = Garcom.objects.all()
        cardapio = Item.objects.all()
        context = {
            "garcons": lista_garcons,
            "cardapio": cardapio
        }
        template = loader.get_template("criar_pedido.html")
        return HttpResponse(template.render(request=request, context=context))