from django.contrib import admin

from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1
    


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao_curta','preco_marketing','preco_marketing_promocional']
    
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
