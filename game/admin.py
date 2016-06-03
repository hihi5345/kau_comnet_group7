from django.contrib import admin

# Register your models here.
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'online']
    class Meta:
        model = Player

admin.site.register(Player, PlayerAdmin)
