from django.http import HttpResponse
from django.template import loader
from ..models import Garcom
from django.shortcuts import redirect

def atualizar_garcom(request, id):
    if request.method == 'POST':
        form = request.POST

        for chave in form:
            item = form[chave]
            if item == None:
                continue
            
            try:
                Garcom.objects.filter(id=id).update(**{chave:item})
            except:
                continue
        return redirect("/garcom?garcom_atualizado=true")

    else:
        template = loader.get_template("atualizar_garcom.html")
        context = {
            "id": id
        }
        return HttpResponse(template.render(request=request, context=context))