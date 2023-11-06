from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Mercancia
from app import db

appmercancia = Blueprint('appmercancia',__name__,template_folder="templates")

@appmercancia.route('/ConsultarMercancias',methods=["GET"])
def consultartodos():
    json = request.get_json()
    mercancias = Mercancia.query.all()
    cad = ""
    for mercancia in mercancias:
        cad = cad + f"id: {mercancia.id}, nombre: {mercancia.nombre}, tipomercancia: {mercancia.tipomercancia}, precio: {mercancia.precio}, edicion: {mercancia.edicion}\n" 

    respuesta =  jsonify(cad)
    return respuesta

@appmercancia.route('/ConsultarMercancia',methods=["GET"])
def consultaruno():
    json = request.get_json()
    mercancia = Mercancia.query.get_or_404(json["id"])
    cad = cad + f"id: {mercancia.id}, nombre: {mercancia.nombre}, tipomercancia: {mercancia.tipomercancia}, precio: {mercancia.precio}, edicion: {mercancia.edicion}\n" 
    respuesta = jsonify(cad)
    return respuesta

@appmercancia.route('/AgregarMercancia',methods=["POST"])
def agregarmercancia():
    json = request.get_json()
    mercancia = Mercancia()
    mercancia.nombre = json["nombre"]
    mercancia.precio = json["precio"]
    mercancia.edicion = json["edicion"]
    mercancia.tipomercancia = json["tipomercancia"]
    db.session.add(mercancia)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"mercancia agregado"})
    return respuesta

@appmercancia.route('/EditarMercancia',methods = ["PUT"])
def editarmercancia():
    json = request.get_json()
    mercancia = Mercancia.query.get_or_404(json["id"])
    mercancia.nombre = json["nombre"]
    mercancia.precio = json["precio"]
    mercancia.edicion = json["edicion"]
    mercancia.tipomercancia = json["tipomercancia"]
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"mercancia editado"})
    return respuesta

@appmercancia.route('/BorrarMercancia',methods=["DELETE"])
def borrarmercancia():
    mercancia = Mercancia.query.get_or_404(request.headers['id'])
    db.session.delete(mercancia)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"mercancia eliminado"})
    return respuesta