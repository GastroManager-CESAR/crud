from django.http import HttpResponse
from django.template import loader
from ..models import Pedido

# contexto = {"pedidos": lista_pedidos}
def listar_pedidos(request):
    if request.method == "GET":
        lista_pedidos = []
        try:
            lista_pedidos = Pedido.objects.all()
        except Pedido.DoesNotExist:
            lista_pedidos = []
        
        pedido_criado = request.GET.get("item_criado", None) != None
        pedido_deletado = request.GET.get("item_deletado", None) != None
        template = loader.get_template("index_pedidos.html")
        context = {
            "pedidos": lista_pedidos
        } 
        return HttpResponse(template.render(request=request, context=context))