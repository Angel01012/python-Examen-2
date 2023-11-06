from Animal import Animal 
from cursorDelPool import CursorDelPool
from Conexion import Conexion
from logger_base import log
from datetime import date

class AnimalDAO:
    _SELECCIONAR = "SELECT * FROM animal ORDER BY id"
    _INSERTAR = "INSERT INTO animal (id,raza,fecha_ingreso,fecha_salida) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE animal SET raza=%s,fecha_ingreso=%s,fecha_salida=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM animal WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            animales = []
            for r in registros:
                animal = Animal(r[0],r[1],r[2],r[3])
                animales.append(animal)
            return animales
    @classmethod
    def insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,animal.Raza, animal.Fecha_Ingreso, animal.Fecha_Salida)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza, animal.Fecha_Ingreso, animal.Fecha_Salida,animal.Id)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    # #insertar
    # animal1 = Animal(id=3,raza="pitbull",fecha_ingreso=date(23,11,1),fecha_salida=date(23,11,6))
    # animalInsertado = AnimalDAO.insertar(animal1)
    # log.debug(f"Alumno Agregados {animalInsertado}") 
    # # #actualizar
    # animal1 = Animal(raza="pitbul2",fecha_ingreso=date(23,11,6),fecha_salida=date(23,11,6),id=1)
    # animalActualizado = AnimalDAO.actualizar(animal1)
    # log.debug(f"alumno Actualizados {animalActualizado}")

    # # #eliminar
    # animal1 = Animal(id=2)
    # animalEliminado = AnimalDAO.eliminar(animal1)
    # log.debug(f"Alumno Eliminados {animalEliminado}")

    #Leer
    animal = AnimalDAO.seleccionar()
    for a in animal:
        log.debug(a)