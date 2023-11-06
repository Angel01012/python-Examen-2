from logger_base import log 

class Animal:
    def __init__(self,id=None,raza=None,fecha_ingreso=None,fecha_salida=None)->None:
        self._id = id
        self._raza = raza
        self._fecha_ingreso = fecha_ingreso
        self._fecha_salida = fecha_salida
    
    def __str__(self) -> str:
        return f"""
        Id: {self._id}
        Raza: {self._raza}
        Fecha de ingreso: {self._fecha_ingreso}
        Fecha de salida: {self._fecha_salida}
        """
    
    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self,id):
        self._id = id

    @property
    def Raza(self):
        return self._raza
    @Raza.setter
    def Raza(self,raza):
        self._raza = raza
    
    @property
    def Fecha_Ingreso(self):
        return self._fecha_ingreso
    @Fecha_Ingreso.setter
    def Fecha_Ingreso(self,fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso
    
    @property
    def Fecha_Salida(self):
        return self._fecha_salida
    @Fecha_Salida.setter
    def Fecha_Salida(self,fecha_salida):
        self._fecha_salida = fecha_salida

if __name__== "__main__":
    animal = Animal(1,"Pitbul","01-11-2023","06-11-2023")
    log.debug(animal)