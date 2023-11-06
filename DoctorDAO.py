from Doctor import Doctor
from cursorDelPool import CursorDelPool
from Conexion import Conexion
from logger_base import log
from datetime import date

class DoctorDAO:
    _SELECCIONAR = "SELECT * FROM doctor ORDER BY id"
    _INSERTAR = "INSERT INTO doctor (id,nombre,telefono) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE doctor SET nombre=%s,telefono=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM doctor WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            doctores = []
            for r in registros:
                doctor = Doctor(r[0],r[1],r[2])
                doctores.append(doctor)
            return doctores
    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Id,doctor.Nombre, doctor.Telefono)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre, doctor.Telefono,doctor.Id)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    doctor1 = Doctor(id=3,nombre="juan",telefono="8672035623")
    doctorInsertado = DoctorDAO.insertar(doctor1)
    log.debug(f"Doctor Agregado {doctorInsertado}") 
    # # # #actualizar
    # doctor1 = Doctor(nombre="jose",telefono="8672035623",id=1)
    # doctorActualizado = DoctorDAO.actualizar(doctor1)
    # log.debug(f"Doctor Actualizado {doctorActualizado}")

    # # # #eliminar
    # doctor1 = Doctor(id=2)
    # doctorEliminado = DoctorDAO.eliminar(doctor1)
    # log.debug(f"Doctor Eliminado {doctorEliminado}")

    #Leer
    doctor = DoctorDAO.seleccionar()
    for a in doctor:
        log.debug(a)