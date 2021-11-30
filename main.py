"""Ejercicio 9"""
import Persistencia_pickle as pp
import car_class
import random as rd

ARCHIVO = "coches_obj.txt"
lista_coches = pp.retrieve(ARCHIVO)
if lista_coches == None:
    lista_coches = []
while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    ancho = input("Ancho de la rueda (en mm): ")
    rodadura = input("Rodadura (% del ancho): ")
    diametro = input("Diametro de la llanta (en pulgadas): ")

    wheel = car_class.Wheel(ancho, rodadura, diametro)
    coche = car_class.Car(marca, modelo, combustible, cilindrada, wheel)
    lista_coches.append(coche)
    print("Presión por defecto de las ruedas: ", wheel.presion)

    coche.wheel.set_pressure(input("Dime que presión quieres en las ruedas: "))
    coche.move_to(rd.random() * 100, rd.random() * 600)
    print("Posición: ", coche.get_pos())
    coche.move_incr(rd.random() * 10,
                    rd.random() * 60)
    print("Posición: ", coche.get_pos())
    del (coche)
    del (wheel)

pp.store(lista_coches, ARCHIVO)
lista_coches = []
print(lista_coches)
lista_coches = pp.retrieve(ARCHIVO)
for car in lista_coches:
    print("Marca, Modelo, Combustible, Cilindrada",
          car.marca, car.modelo, car.combustible, car.cilindrada)
    print("Info rueda: ancho, rodadura, diametro, presión => ", car.wheel.print_info())
    print("Posición: ", car.get_pos(), "\n")


