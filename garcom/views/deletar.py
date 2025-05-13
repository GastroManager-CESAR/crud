from django.http import HttpResponse
from django.template import loader
from ..models import Garcom

def deletar_item(request, id):
    if request.method == 'DELETE': 
        try:
            Garcom.objects.filter(id=id).delete()
        except:
            return HttpResponse("Algo deu errado")
        finally:
            return HttpResponse("Item deletado")
        