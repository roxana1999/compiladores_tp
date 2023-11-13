# -*- coding: utf-8 -*-
import sys
def generar_tabla_transiciones(gramatica, tabla, terminales, no_terminales):
    for key, value in gramatica.items():
        estado_inicial = 0
        print "la clave es " + key
        lista_producciones = value
        for produccion in lista_producciones:
            estado_actual = estado_inicial
            print "la produccion es " + str(produccion)
            for i,c in enumerate(produccion):
                print "c es " + c
                if c in terminales:
                    posicion_terminal = terminales.index(c)+1
                    estado_siguiente = len(tabla) - 1
                    fila_actual = tabla[estado_actual+1]
                    lista_estados = fila_actual[posicion_terminal]
                    lista_estados.append(estado_siguiente)                    
                    nueva_fila = []
                    nueva_fila.append(estado_siguiente)
                    for t in terminales:
                        nueva_fila.append([])
                    nueva_fila.append([]) # para la transicion epsilon
                    tabla.append(nueva_fila)
                    estado_actual = estado_siguiente
                elif c == 'epsilon':
                    posicion_terminal = len(terminales)+1
                    fila_actual = tabla[estado_actual+1]
                    lista_estados = fila_actual[posicion_terminal]
                    estado_siguiente = len(tabla) - 1
                    lista_estados.append(estado_siguiente)
                    nueva_fila = []
                    nueva_fila.append(estado_siguiente)
                    for t in terminales:
                        nueva_fila.append([])
                    nueva_fila.append([]) # para la transicion epsilon
                    tabla.append(nueva_fila)
                    estado_actual = estado_siguiente
                elif c in no_terminales:
                    posicion_terminal = len(terminales)+1
                    fila_actual = tabla[estado_actual+1]
                    lista_estados = fila_actual[posicion_terminal]
                    if i == len(produccion) - 1:
                        print "cumple la codicion"
                        lista_estados.append(estado_actual)
                    else:
                        print "no cumple la condicion"
                        estado_siguiente = len(tabla) - 1
                        lista_estados.append(estado_siguiente)
                        nueva_fila = []
                        nueva_fila.append(estado_siguiente)
                        for t in terminales:
                            nueva_fila.append([])
                        nueva_fila.append([]) # para la transicion epsilon
                        tabla.append(nueva_fila)
                        estado_actual = estado_siguiente
                            # no voy a hacer recursion por el momento
        break
    
    print "im done for now"

def generar_gramatica_1():
    terminales = ['0','1']
    no_terminales = ['S']
    tabla_transiciones = [['','0','1', 'epsilon'], [0, [], [], []]];
    e1 = ['0', 'S', '1']
    e2 = ['0', '1']
    e3 = ['1', '0']
    e4 = ['epsilon']
    lista_producciones = [e1, e2, e3, e4]
    gramatica_1 = {'S' : lista_producciones}

    generar_tabla_transiciones(gramatica_1, tabla_transiciones, terminales, no_terminales)
    for fila in tabla_transiciones:
        for item in fila:
            print("{:>{}}".format(str(item)+"|", 10)),
        print "\n----------------------------------------------------"
generar_gramatica_1()