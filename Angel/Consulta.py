from logger_base import log 

class Consulta:
    def __init__(self,id_animal=None,id_doctor=None,servicio=None, costo=None)->None:
        self._id_animal = id_animal
        self._id_doctor = id_doctor
        self._servicio = servicio
        self._costo = costo
    
    def __str__(self) -> str:
        return f"""
        Id Animal: {self._id_animal}
        Id Doctor: {self._id_doctor}
        servicio: {self._servicio}
        Costo: {self._costo}
        """
    
    @property
    def Id_Animal(self):
        return self._id_animal
    @Id_Animal.setter
    def Id_Animal(self,Id_Animal):
        self._id_animal = Id_Animal

    @property
    def Id_Doctor(self):
        return self._id_doctor
    @Id_Doctor.setter
    def Id_Doctor(self,Id_Doctor):
        self._id_doctor = Id_Doctor
    
    @property
    def Servicio(self):
        return self._servicio
    @Servicio.setter
    def Servicio (self,Servicio):
        self._servicio = Servicio
    
    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo (self,Costo):
        self._costo = Costo

if __name__== "__main__":
    consulta = Consulta(1,1,"chequeo",192.5)
    log.debug(consulta)