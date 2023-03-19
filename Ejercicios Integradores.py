"""Ejercicios integradores para revisar en la clase 7
1. Escribir una función que calcule el máximo común divisor entre dos números."""

def maximoComunDivisor(Numerouno,Numerodos):
    if Numerodos == 0: 
        return Numerouno
    else:
        return maximoComunDivisor(Numerodos, Numerouno % Numerodos )
    
Numerouno = int(input("valor A\n"))
Numerodos = int(input("valor B\n"))
print("maximo Comun Divisor")
print(maximoComunDivisor(Numerouno,Numerodos))


"""2. Escribir una función que calcule el mínimo común múltiplo entre dos números"""

def minimoComunMultiplo(Numerouno, Numerodos):
    return ((Numerouno * Numerodos) // maximoComunDivisor(Numerouno, Numerodos))
print("minimo comun multiplo")
print(minimoComunMultiplo(Numerouno,Numerodos))

"""3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."""


def cantidaDePalabras(texto):
    frecuencia = {}
    palabras = texto.split()
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
texto= input("ingrese el texto\n")   
diccionario=cantidaDePalabras(texto)
print(diccionario)

"""4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia."""
def PalabraMasRepetida(diccionario):
    MasPalabra = ""
    MayorFrecuencia = 0
    for palabra, cantidad in diccionario.items():
        if cantidad > MayorFrecuencia:
            MasPalabra = palabra
            MayorFrecuencia = cantidad
    return (MasPalabra, MayorFrecuencia)

print(PalabraMasRepetida(cantidaDePalabras(texto)))
"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva."""
def get_int():
    #while True: #si se elije poner el while entonces no es necesario  el volver llamar a la funcion
    try:
        valorEntero = int(input("Ingrese un valor entero"))
        return valorEntero
    except ValueError:
        print ("No ha ingresado un numero entero")
        return get_int
    

"""6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""
class Persona:
    def __init__(self,nombre, edad,dni):
        self.__nombre= nombre
        self.__edad = edad
        self.__dni = dni
    def get_edad(self):
        return self.__edad   
    
    def get_nombre(self):
        return self.__nombre   
    
    def get_dni(self):
        return self.__dni   
    
    def set_nombre(self, nombre):
         self.__nombre= nombre
    
    def set_dni(self, dni):
        if len(dni) == 8:
         self.__dni= dni
    
    def set_nombre(self, edad):
        if edad >= 0:
         self.__edad= edad
         

    def mostrar (self):
        print("Nombre", self.__nombre)
        print("edad", self.__edad)
        print("dni", self.__dni)
    def Es_mayor_de_edad(self):
        return self.__edad > 17

"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos."""
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad
   
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

    def mostrar (self):
        print("Nombre", self.titular)
        print("cantidad", self.__Cantidad)

#cuenta_pepe = Cuenta(Persona("Pepe", 30),0)

     
"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta"""
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        edad = self.get_titular().get_edad()
        return edad >= 18 and edad < 25

    def mostrar(self):
        super().mostrar()
        print("Cuenta Joven")
        print(self.__bonificacion, "%")
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
