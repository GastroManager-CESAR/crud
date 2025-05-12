from django.http import HttpResponse
from django.template import loader
from ..models import Item


def deletar(request, id):
    if request.method == 'DELETE':
        try:
            Item.objects.filter(id=id).delete()
        except:
            return HttpResponse("Algo deu errado")
        finally:
            return HttpResponse("Item deletado")
