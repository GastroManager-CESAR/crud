from django.http import HttpResponse
from django.shortcuts import redirect
from ..models import Pedido
from django.template import loader
from django.shortcuts import redirect

def deletar_pedido(request, id):
    if request.method == "GET":
        try:
            Pedido.objects.filter(id=id).delete()
        except:
            return HttpResponse("Deu Erro!!!")
        finally:
            return redirect("/pedidos?pedido_deletado=true")
        