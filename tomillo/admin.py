from django.contrib import admin
from .models import *

from translations.admin import TranslatableAdmin, TranslationInline


admin.site.register(Numero)
admin.site.register(Aliado)
admin.site.register(Programa)
admin.site.register(Promocion)
admin.site.register(Alumni)
admin.site.register(Prensa)
admin.site.register(Publicacion)
admin.site.register(Recurso)


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]

