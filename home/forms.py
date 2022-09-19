from django.forms import ModelForm
from .models import equipos
from .models import estadios
from .models import jugadores



class equiposform(ModelForm):
    class Meta:
        model = equipos
        fields = '__all__'


class estadiosform(ModelForm):
    class Meta:
        model = estadios
        fields = '__all__'


class jugadoresform(ModelForm):
    class Meta:
        model = jugadores
        fields = '__all__'