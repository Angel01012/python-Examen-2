from Animal import Animal 
from Consulta import Consulta
from Doctor import Doctor
from Consulta import Consulta
from cursorDelPool import CursorDelPool
from Conexion import Conexion
from logger_base import log
from datetime import date

class ConsultasDAO:
    _SELECCIONAR = "SELECT a.raza, d.nombre, servicio, costo  FROM consulta as c, animal as a, doctor as d ORDER BY id_animal"
    _INSERTAR = "INSERT INTO consulta (id_animal, id_doctor,servicio, costo) VALUES (%s,%s,%s,%s)"

    @classmethod
    def seleccionartodos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consultas = []
            for r in registros:
                con = Consulta(r[0],r[1],r[2],r[3])
                consultas.append(con)
            return consultas
    # @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Id_Animal, consulta.Id_Doctor, consulta.Servicio, consulta.Costo)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

        
if __name__ == "__main__":
    # #insertar
    consulta1 = Consulta(id_animal=1, id_doctor=1, servicio="esterilizacion", costo=1550.10)
    consultaInsertada = ConsultasDAO.insertar(consulta1)
    log.debug(f"Consulta Agregado {consultaInsertada}") 
    # #Leer
    consulta = ConsultasDAO.seleccionartodos()
    for c in consulta:
        log.debug(c)