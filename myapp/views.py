from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Usuario



# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
           print('error')
       context = {}
       return render(request, self.template_name, context=context)


def tabla_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'users.html', {'usuarios': usuarios})

class RegistroView(TemplateView):
    template_name = 'registro.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

