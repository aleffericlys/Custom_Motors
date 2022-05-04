from django.contrib import admin

from .models import Mensages, Motos, Acessorios, Ferramentas

admin.site.register(Motos)
admin.site.register(Acessorios)
admin.site.register(Mensages)
admin.site.register(Ferramentas)
# Register your models here.
