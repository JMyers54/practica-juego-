
class Usuario():
    def __init__(self,Nombre,Apellido,Edad,Sexo,Contraseña,Gmail):
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Edad = Edad
        self.__Sexo = Sexo
        self.__Contraseña = Contraseña
        self.__Gmail = Gmail

    @property
    def Nombre(self): return self.__Nombre

    @property
    def Apellido(self): return self.__Apellido
    
    @property
    def Edad(self): return self.__Edad
    
    @property
    def Sexo(self): return self.__Sexo
    
    @property
    def Contraseña(self): return self.__Contraseña
    
    @property
    def Gmail(self): return self.__Gmail


    def Iniciar_Sesion(self):
        pass

    def Registrar(self):
        pass
    