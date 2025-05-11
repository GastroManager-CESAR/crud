from django.http import HttpResponse
from django.template import loader
from .models import Item
# Create your
#  views here.

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def criar_item(request):
    if request.method == 'POST':
        form = request.POST
        
        titulo = form['titulo']
        descricao = form['descricao']
        
        operacao = Item(titulo=titulo, descricao=descricao)
        try:
            operacao.save()
        except:
            return HttpResponse("Deu erro")
        finally:
            return HttpResponse("Obrigado por se cadastrar")

    else:
        return HttpResponse("Inválido")