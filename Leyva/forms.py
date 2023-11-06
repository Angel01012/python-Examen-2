from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms .validators import DataRequired

class EquipoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    cantidadjugadores = StringField('cantidadjugadores')
    precioactual = StringField('precioactual')
    liga = StringField('liga')
    enviar = SubmitField("Enviar")
