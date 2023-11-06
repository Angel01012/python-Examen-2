from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Equipo
from forms import EquipoForm
from app import db

appequipo = Blueprint('appequipo',__name__,template_folder="templates")

@appequipo.route('/')
def inicio():
    return render_template("index.html")

@appequipo.route('/listadoequipo')
def listadoEquipo():
    equipos = Equipo.query.all()
    return render_template('listadoEquipos.html',equipos=equipos)

@appequipo.route('/agregarequipo',methods=["GET","POST"])
def agregarEquipo():
    equipo = Equipo()
    equipoform = EquipoForm(obj=equipo)
    if request.method == "POST":
        if equipoform.validate_on_submit():
            equipoform.populate_obj(equipo)
            db.session.add(equipo)
            db.session.commit()
            return redirect(url_for('appequipo.listadoEquipo'))
    return render_template('agregarEquipo.html',forma=equipoform)

@appequipo.route('/editarequipo/<int:id>',methods=["GET","POST"])
def editarEquipo(id):
    equipo = Equipo.query.get_or_404(id)
    equipoform = EquipoForm(obj=equipo)
    if request.method == "POST":
        if equipoform.validate_on_submit():
            equipoform.populate_obj(equipo)
            db.session.commit()
            return redirect(url_for('appequipo.listadoEquipo'))
    return render_template('editarEquipo.html',forma=equipoform)

@appequipo.route('/eliminarequipo/<int:id>', methods=["POST","GET"])
def eliminarEquipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('appequipo.listadoEquipo'))

@appequipo.route('/consultarequipo/<int:id>',methods=["GET","POST"])
def consultarEquipo(id):
    equipo = Equipo.query.get_or_404(id)
    equipos = [equipo]
    #productoform = ProductosForm(obj=producto)
    
    return render_template('consultarEquipo.html',equipos=equipos)

@appequipo.route('/404')
def Error():
    render_template('404.html')


