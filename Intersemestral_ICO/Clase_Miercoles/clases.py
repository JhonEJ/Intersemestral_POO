class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = carr

    def set_nommbre(self,nom):
        self.__nombre=nom

    def get_nommbre(self):
        return self.__nombre

    def set_edad(self,ed):
        if ed >= 8 and ed <= 120:
            self.__edad=ed
        else:
            print("esa edad no es correcta")
        self.__edad=ed

    def get_edad(self):
        return self.__edad

    def set_carrera(self,carr):
        self.__carrera=carr

    def get_carrera(self):
        return  self.__carrera

    def __str__(self):
        cadena = "-------\n Nombre: "+self.__nombre
        cadena = cadena+"\n Edad: "+ str(self.__edad)
        cadena = cadena+"\n Carrera: "+ self.__carrera
        cadena = cadena+"\n--------"
        return cadena

    def estudiar (self,horas=1):
        print(f"El alumno{self.__nombre} esta estudianto por {horas} horas ")


