from flask import Blueprint,request,redirect,render_template,url_for,jsonify
from models import Patrocinador
from app import db

apppatrocinador = Blueprint('apppatrocinador',__name__,template_folder="templates")

@apppatrocinador.route('/ConsultarPatrocinadores',methods=["GET"])
def consultartodos():
    json = request.get_json()
    patrocinadores = Patrocinador.query.all()
    cad = ""
    for patrocinador in patrocinadores:
        cad = cad + f"id: {patrocinador.id}, nombre: {patrocinador.nombre}, presupuesto: {patrocinador.presupuesto}, añoscontratado: {patrocinador.añoscontratado}, pais: {patrocinador.pais}\n" 

    respuesta =  jsonify(cad)
    return respuesta

@apppatrocinador.route('/ConsultarPatrocinador',methods=["GET"])
def consultaruno():
    json = request.get_json()
    patrocinador = Patrocinador.query.get_or_404(json["id"])
    cad = cad + f"id: {patrocinador.id}, nombre: {patrocinador.nombre}, presupuesto: {patrocinador.presupuesto}, añoscontratado: {patrocinador.añoscontratado}, pais: {patrocinador.pais}\n" 
    respuesta = jsonify(cad)
    return respuesta

@apppatrocinador.route('/AgregarPatrocinador',methods=["POST"])
def agregarpatrocinador():
    json = request.get_json()
    patrocinador = Patrocinador()
    patrocinador.nombre = json["nombre"]
    patrocinador.presupuesto = json["presupuesto"]
    patrocinador.añoscontratado = json["añoscontratado"]
    patrocinador.pais = json["pais"]
    db.session.add(patrocinador)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"patrocinador agregado"})
    return respuesta

@apppatrocinador.route('/EditarPatrocinador',methods = ["PUT"])
def editarpatrocinador():
    json = request.get_json()
    patrocinador = Patrocinador.query.get_or_404(json["id"])
    patrocinador.nombre = json["nombre"]
    patrocinador.presupuesto = json["presupuesto"]
    patrocinador.añoscontratado = json["añoscontratado"]
    patrocinador.pais = json["pais"]
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"patrocinador editado"})
    return respuesta

@apppatrocinador.route('/BorrarPatrocinador',methods=["DELETE"])
def borrarpatrocinador():
    patrocinador = Patrocinador.query.get_or_404(request.headers['id'])
    db.session.delete(patrocinador)
    db.session.commit()
    respuesta = jsonify({"status":200,"mensaje":"patrocinador eliminado"})
    return respuesta