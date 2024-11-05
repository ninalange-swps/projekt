from django.contrib import admin

# Register your models here.
from .models import Stanowisko, Osoba

@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko_id_display', 'data_dodania')
    readonly_fields = ('data_dodania',)

    @admin.display(description='Stanowisko (id)')
    def stanowisko_id_display(self, obj):
        return f"{obj.stanowisko} ({obj.stanowisko.id})"

