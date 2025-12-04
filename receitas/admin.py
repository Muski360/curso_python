from django.contrib import admin
from .models import Categoria, Receita

# Register your models here.

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...

class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Categoria, CategoriaAdmin)