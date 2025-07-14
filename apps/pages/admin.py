from django.contrib import admin
from .models import Projeto, Certificado, Contato

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em', 'atualizado_em')
    search_fields = ('nome',)

@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'projeto', 'emitido_em')
    search_fields = ('nome', 'projeto__nome')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')