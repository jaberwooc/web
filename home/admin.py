from django.contrib import admin
from .models import equipos
from .models import jugadores
from .models import estadios

# Register your models here.
admin.site.register(equipos)
admin.site.register(jugadores)
admin.site.register(estadios)