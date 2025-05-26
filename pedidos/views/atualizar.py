from django.http import HttpResponse
from django.template import loader
from ..models import Pedido
from django.shortcuts import redirect
from garcom.models import Garcom
from menu.models import Item

def atualizar_pedido(request, id):
    if request.method == 'POST':
        form = request.POST

        for chave in form:
            pedidos = form[chave]
            if pedidos == None:
                continue
            try:
                Pedido.objects.filter(id=id).update(**{chave:pedidos})
            except:
                continue
        return redirect("/pedidos?pedido_atualizado=true")

    else:
        template = loader.get_template("atualizar_pedido.html")
        lista_garcons = Garcom.objects.all()
        cardapio = Item.objects.all()
        context = {
            "id": id,
            "garcons": lista_garcons,
            "cardapio": cardapio
        }
        
        return HttpResponse(template.render(request=request, context=context))