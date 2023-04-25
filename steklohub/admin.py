from django.contrib import admin
from .models import Peregorodki, Kozirki, Nerjograda, Stekloograda, Interer



@admin.register(Peregorodki)
class PeregorodkiAdmin(admin.ModelAdmin):
    list_display = ['picture']

@admin.register(Kozirki)
class KozirkiAdmin(admin.ModelAdmin):
    list_display = ['picture']

@admin.register(Nerjograda)
class NerjogradaAdmin(admin.ModelAdmin):
    list_display = ['picture']

@admin.register(Stekloograda)
class StekloogradaAdmin(admin.ModelAdmin):
    list_display = ['picture']

@admin.register(Interer)
class IntererAdmin(admin.ModelAdmin):
    list_display = ['picture']

