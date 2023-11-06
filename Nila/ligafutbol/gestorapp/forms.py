from  django.forms import ModelForm,EmailInput
from gestorapp.models import *

class Equipoform(ModelForm):
    class Meta:
        model = Equipo
        fields = "_all_"
        widgets={
            'email':EmailInput(
                attrs ={
                    'type': 'email',
                    'class': 'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }


class Ligaform(ModelForm):
    class Meta:
        model = Liga
        fields = "_all_"
        widgets={
            'email':EmailInput(
                attrs ={
                    'type': 'email',
                    'class': 'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }


class Patrocinadorform(ModelForm):
    class Meta:
        model = Patrocinador
        fields = "_all_"
        widgets={
            'email':EmailInput(
                attrs ={
                    'type': 'email',
                    'class': 'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }


class Jugadorform(ModelForm):
    class Meta:
        model = Jugador
        fields = "_all_"
        widgets={
            'email':EmailInput(
                attrs ={
                    'type': 'email',
                    'class': 'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }


class Partidoform(ModelForm):
    class Meta:
        model = Partido
        fields = "_all_"
        widgets={
            'email':EmailInput(
                attrs ={
                    'type': 'email',
                    'class': 'form-control',
                    'style': 'max-width:100px',
                    'placeholder':'Correo'
                }
            )
        }