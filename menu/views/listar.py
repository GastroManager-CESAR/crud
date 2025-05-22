from django.http import HttpResponse
from django.template import loader
from ..models import Item

def listar_item(request):
    if request.method == "GET":
        lista_item = []
        try:
            lista_item = Item.objects.all()
        except Item.DoesNotExist:
            lista_item = []
        item_criado = request.GET.get("item_criado", None) != None
        item_deletado = request.GET.get("item_deletado", None) != None
        context = {
            "cardapio": lista_item,
            "item_criado": item_criado,
            "item_deletado": item_deletado
        }
        template = loader.get_template("index.html")
        return HttpResponse(template.render(request=request, context=context))