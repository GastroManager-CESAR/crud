from django.http import HttpResponse
from django.template import loader
from ..models import Garcom

def listar_garcom(request):
    if request.method == "GET":
        lista_garcom = []
        try:
            lista_garcom = Garcom.objects.all()
        except Garcom.DoesNotExist:
            lista_garcom = []
        garcom_criado = request.GET.get("garcom_criado", None) != None
        garcom_deletado = request.GET.get("garcom_deletado", None) != None
        context = {
            "garcons": lista_garcom,
            "garcom_criado": garcom_criado,
            "garcom_deletado": garcom_deletado
        }
        template = loader.get_template("index_garcom.html")
        return HttpResponse(template.render(request=request, context=context))