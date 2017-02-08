#!/usr/bin/python

fich = open("/etc/passwd", "r")
lineas = fich.readlines()
fich.close()

shells = {}
for linea in lineas:
    user = linea.split(":")[0]
    shell = linea.split(":")[-1][:-1]
    shells[user] = shell

usuariosPrueba = ['root', 'imaginario']
for usuario in usuariosPrueba:
    try:
        print(shells[usuario])
    except KeyError:
        print("El usuario " + usuario + " no existe")
