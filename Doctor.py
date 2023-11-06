from logger_base import log 

class Doctor:
    def __init__(self,id=None,nombre=None,telefono=None)->None:
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
    
    def __str__(self) -> str:
        return f"""
        Id: {self._id}
        Nombre: {self._nombre}
        Telefono: {self._telefono}
        """
    
    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self,Id):
        self._id = Id

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def Telefono(self):
        return self._telefono
    @Telefono.setter
    def Telefono (self,Telefono):
        self._telefono = Telefono

if __name__== "__main__":
    doctor = Doctor(1,"Juan","8672809248")
    log.debug(doctor)