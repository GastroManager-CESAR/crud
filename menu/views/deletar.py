from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from ..models import Item


def deletar_item(request, id):
    if request.method == 'GET':
        try:
            Item.objects.filter(id=id).delete()
        except:
            return HttpResponse("Algo deu errado")
        finally:
            return redirect("/menu?item_deletado=true")
