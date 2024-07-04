class  persona():

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre = nombre
        self.edad= edad
        self.dni= dni


    def set_nombre(self,nombre):
        if nombre.strip() == "":
            print("El nombre no puedo estar vacio")
        else:
            self.nombre = nombre

    def set_edad(self,edad):

        try:
            edad = int(edad)
            if edad <= 0:
                print("La edad no puede ser 0 o un numero negativo ")
            else:
                self.edad = edad
        except ValueError:
            print("La edad tiener que ser un numero entero")

    def set_dni(self,dni):
        if len(dni) != 8:
            print("El dni tiene que tener 8 caracteres")
        else:
            self.dni = dni

    def get_nombre(self):
        return print("El nombre de la persona es : {}".format(self.nombre))

    def get_edad(self):
        return print("La edad es : {}".format(self.edad))

    def get_dni(self):
        return print("El dni es : {}".format(self.dni))

    def mostrar(self):
         self.get_nombre()
         self.get_edad()
         self.get_dni()


persona = persona()
persona.set_nombre("hola")
persona.set_edad(9)
persona.set_dni("12345613")
persona.mostrar()