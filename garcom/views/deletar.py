from django.http import HttpResponse
from django.shortcuts import redirect
from ..models import Garcom

def deletar_garcom(request, id):
    if request.method == 'GET': 
        try:
            Garcom.objects.filter(id=id).delete()
        except:
            return HttpResponse("Algo deu errado")
        finally:
            return redirect("/garcom?garcom_deletado=true")