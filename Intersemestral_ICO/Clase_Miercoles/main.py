from Clase_Miercoles.clases import Alumno

def main():
    al1=Alumno("Jose",19,"ico")
    al2 = Alumno("Maria", 25, "ico")
    print(vars(al1))
    al1.__nombre="Diego"
    print(vars(al1))

    print(al1)
    print(al2)
    al1.estudiar(4)

main()
