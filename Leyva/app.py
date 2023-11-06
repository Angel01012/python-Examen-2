from flask import Flask,render_template
from database import db
from config import BasicConfig
from flask_migrate import Migrate
from routes.Equipo.equipo import appequipo
from routes.Jugador.jugador import appjugador
from routes.Mercancia.mercancia import appmercancia
from routes.Partido.partido import apppartido
from routes.Patrocinador.patrocinador import apppatrocinador
import logging

app = Flask(__name__)
app.register_blueprint(appequipo)
app.register_blueprint(appjugador)
app.register_blueprint(appmercancia)
app.register_blueprint(apppartido)
app.register_blueprint(apppatrocinador)

app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)

logging.basicConfig(level=logging.DEBUG,filename="debug.log")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')